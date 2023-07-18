import tkinter as tk
import time
import serial
import threading

# Serial setup
serial_port = 'COM3'
baud_rate = 9600

# Arduino pin config
pin_a_high = 30
pin_a_low = 31
pin_b_high = 28
pin_b_low = 29
pin_c_high = 26
pin_c_low = 27
pin_d_high = 24
pin_d_low = 25
pin_e_high = 22
pin_e_low = 23

# Keep track of changes
changes_made = False
# Serial connection status
is_connected = False
# Create Serial object for reading and writing
arduino = None

# Light indicator colors for changes
light_off_color = "gray"
light_red_color = "red"
light_green_color = "green"

def update_light_indicator():
    '''Updates the color of the light indicator based on changes_made'''
    if changes_made:
        light_indicator.config(bg=light_red_color)
    else:
        light_indicator.config(bg=light_green_color)

# Create a separate thread for reading from the serial port
def read_serial():
    '''Function to continuously read from the serial port'''
    global arduino
    arduino = serial.Serial(serial_port, baud_rate)
    while True:
        if arduino.in_waiting > 0:
            serial_data = arduino.readline().decode().strip()
            print(serial_data)

serial_thread = threading.Thread(target=read_serial)
serial_thread.daemon = True
serial_thread.start()

# Other useful functions
def connect_arduino():
    '''Establishes a serial connection with the Arduino'''
    global is_connected, arduino
    try:
        arduino = serial.Serial(serial_port, baud_rate)
        arduino.close()
        time.sleep(2)  # Add a delay to allow the Arduino to reset
        arduino.open()  # Reopen the serial connection
        is_connected = True
        print("Serial connection established.")
    except serial.SerialException as e:
        pass
        #print("Serial port connection error:", e)

def input_command(checkboxes, checkbox_names):
    '''Function to send serial input to Arduino'''
    global changes_made, is_connected, arduino
    if changes_made:
        if not is_connected:    
            connect_arduino()
        try:
            for checkbox_var, name in zip(checkboxes, checkbox_names):
                if checkbox_var.get():
                    print(f"Sending command: {name}")
                    arduino.write(f'{name}'.encode())
            changes_made = False
            update_apply_button_state()
            update_light_indicator()
        except serial.SerialException:
            print("Serial port connection error.")

def apply_changes():
    '''Applies the configuration of checkboxes at the time of clicking the button'''
    global changes_made
    input_command(checkboxes, checkbox_names)

def create_checkbox(window, text, name, mutually_exclusive_checkboxes, row):
    '''Creates checkboxes in grid and fills a list of all checkboxes'''
    checkbox_var = tk.BooleanVar()
    checkbox = tk.Checkbutton(window, text=text, variable=checkbox_var,
                              command=lambda: toggle_checkboxes(checkboxes, mutually_exclusive_checkboxes,
                                                               checkbox_var))
    checkbox.grid(row=row, column=1, sticky='w')
    checkboxes.append(checkbox_var)
    checkbox_names.append(name)
    return checkbox_var

def toggle_checkboxes(checkboxes, mutually_exclusive_checkboxes, current_checkbox):
    '''Allows mutual exclusivity of specified checkboxes'''
    if current_checkbox.get():
        for checkbox in mutually_exclusive_checkboxes:
            if checkbox != current_checkbox:
                checkbox.set(False)

def update_apply_button_state():
    '''Updates the state of the Apply button based on changes_made'''
    if changes_made:
        apply_button.config(state='normal')
    else:
        apply_button.config(state='disabled')

checkboxes = []
checkbox_names = []

# Create a new tkinter window
window = tk.Tk()
frame = tk.Frame(window)
frame.grid(row=0, column=0, padx=10, pady=10)

# All Electrodes
row = 0
bold_font = ('Helvetica', 16, 'bold')
tk.Label(frame, text="All Electrodes:", font=bold_font).grid(row=row, column=0, pady=10)

row += 1
label_font = ('Helvetica', 12)
all_high_var = create_checkbox(frame, "All High", "all high", checkboxes, row)

row += 1
label_font = ('Helvetica', 12)
all_low_var = create_checkbox(frame, "All Low", "all low", checkboxes, row)

row += 1
label_font = ('Helvetica', 12)
all_off_var = create_checkbox(frame, "All Off", "all off", checkboxes, row)

# Electrode Set 'a'
a_mutex = [all_high_var, all_low_var, all_off_var]

row += 1
bold_font = ('Helvetica', 16, 'bold')
tk.Label(frame, text="Electrode Set 'a':", font=bold_font).grid(row=row, column=0, pady=10)

row += 1
label_font = ('Helvetica', 12)
a_high_var = create_checkbox(frame, "High", "a high", a_mutex, row)
a_mutex.append(a_high_var)

row += 1
label_font = ('Helvetica', 12)
a_low_var = create_checkbox(frame, "Low", "a low", a_mutex, row)
a_mutex.append(a_low_var)

row += 1
label_font = ('Helvetica', 12)
a_off_var = create_checkbox(frame, "Off", "a off", a_mutex, row)
a_mutex.append(a_off_var)

# Electrode Set 'b'
b_mutex = [all_high_var, all_low_var, all_off_var]

row += 1
bold_font = ('Helvetica', 16, 'bold')
tk.Label(frame, text="Electrode Set 'b':", font=bold_font).grid(row=row, column=0, pady=10)

row += 1
label_font = ('Helvetica', 12)
b_high_var = create_checkbox(frame, "High", "b high", b_mutex, row)
b_mutex.append(b_high_var)

row += 1
label_font = ('Helvetica', 12)
b_low_var = create_checkbox(frame, "Low", "b low", b_mutex, row)
b_mutex.append(b_low_var)

row += 1
label_font = ('Helvetica', 12)
b_off_var = create_checkbox(frame, "Off", "b off", b_mutex, row)
b_mutex.append(b_off_var)

# Electrode Set 'c'
c_mutex = [all_high_var, all_low_var, all_off_var]

row += 1
bold_font = ('Helvetica', 16, 'bold')
tk.Label(frame, text="Electrode Set 'c':", font=bold_font).grid(row=row, column=0, pady=10)

row += 1
label_font = ('Helvetica', 12)
c_high_var = create_checkbox(frame, "High", "c high", c_mutex, row)
c_mutex.append(c_high_var)

row += 1
label_font = ('Helvetica', 12)
c_low_var = create_checkbox(frame, "Low", "c low", c_mutex, row)
c_mutex.append(c_low_var)

row += 1
label_font = ('Helvetica', 12)
c_off_var = create_checkbox(frame, "Off", "c off", c_mutex, row)
c_mutex.append(c_off_var)

# Electrode Set 'd'
d_mutex = [all_high_var, all_low_var, all_off_var]

row += 1
bold_font = ('Helvetica', 16, 'bold')
tk.Label(frame, text="Electrode Set 'd':", font=bold_font).grid(row=row, column=0, pady=10)

row += 1
label_font = ('Helvetica', 12)
d_high_var = create_checkbox(frame, "High", "d high", d_mutex, row)
d_mutex.append(d_high_var)

row += 1
label_font = ('Helvetica', 12)
d_low_var = create_checkbox(frame, "Low", "d low", d_mutex, row)
d_mutex.append(d_low_var)

row += 1
label_font = ('Helvetica', 12)
d_off_var = create_checkbox(frame, "Off", "d off", d_mutex, row)
d_mutex.append(d_off_var)

# Electrode Set 'e'
e_mutex = [all_high_var, all_low_var, all_off_var]

row += 1
bold_font = ('Helvetica', 16, 'bold')
tk.Label(frame, text="Electrode Set 'e':", font=bold_font).grid(row=row, column=0, pady=10)

row += 1
label_font = ('Helvetica', 12)
e_high_var = create_checkbox(frame, "High", "e high", e_mutex, row)
e_mutex.append(e_high_var)

row += 1
label_font = ('Helvetica', 12)
e_low_var = create_checkbox(frame, "Low", "e low", e_mutex, row)
e_mutex.append(e_low_var)

row += 1
label_font = ('Helvetica', 12)
e_off_var = create_checkbox(frame, "Off", "e off", e_mutex, row)
e_mutex.append(e_off_var)

# Apply button
row += 1
apply_button = tk.Button(frame, text="Apply", font=('Helvetica', 12), command=apply_changes, state='disabled')
apply_button.grid(row=row, column=2, pady=20)

# Light indicator for changes
light_indicator = tk.Label(frame, bg=light_off_color, width=2)
light_indicator.grid(row=row, column=3, padx=10)


# Function to continuously check for changes
def check_changes():
    global changes_made
    previous_state = [checkbox.get() for checkbox in checkboxes]
    while True:
        current_state = [checkbox.get() for checkbox in checkboxes]
        if current_state != previous_state:
            changes_made = True
            update_apply_button_state()
            update_light_indicator()
            previous_state = current_state
        time.sleep(0.1)


changes_thread = threading.Thread(target=check_changes)
changes_thread.daemon = True
changes_thread.start()


# Start the main loop
window.mainloop()
print('Window closed.')
arduino.write('all off'.encode())
