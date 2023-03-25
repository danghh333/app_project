import sqlite3

def add_printer(name, manufacturer, model, serial_num, firmware_vers, calibration, date):
    """Add all the information of the 3D printer machine"""
    con = sqlite3.connect('3d_printer_machine_management.db')
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS printer (name TEXT, manufacturer TEXT, model TEXT, serial_num INTEGER, firmware_vers TEXT, calibration TEXT, date DATE)')
    con.commit()
    con.close()
