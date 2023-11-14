import tkinter as tk # the GUI toolbox
import pyproj # library for geospatial, including calculating the distance between points
import regex # library for input validation function


root = tk.Tk()  # must match the bottom two lines of code in order for this to work

# The names of the four variables to be input, allows floats to deal with lat and long
# the latitude of point 1
p1lat = tk.StringVar()
# the longitude of point 1
p1long = tk.StringVar()
# the latitude of point 2
p2lat = tk.StringVar()
# the longitude of point 2
p2long = tk.StringVar()



class Window(tk.Frame):

    def __init__(self, master=None):

        tk.Frame.__init__(self, master)

        self.master = master

        self.pack()


        # The GUI can be dragged larger or smaller horizontally or vertically, True for resizable, False for fixed
        self.master.resizable(True, True)

        # sets the fonts to be used in this GUI

        title_font = ('Arial', 16)

        font = ('Arial', 10)

        # Improved color
        self.master.tk_setPalette(background='#ececec')

        # Title
        self.master.title("Distance calculator")

        # Positions the GUI in the screen sweet spot

        x = (self.master.winfo_screenwidth() -
             self.master.winfo_reqwidth()) / 2
        y = (self.master.winfo_screenheight() -
             self.master.winfo_reqheight()) / 3
        x = str(int(x))
        y = str(int(y))

        self.master.geometry("+{}+{}". format(x, y))

        def validate(string):
            regex = re.compile(r"[0-9.-]*$")
            result = regex.match(string)
            return (string != ""
                and string.count('.') <= 1
                and string.count('-') <= 1
                and result is not None
                and result.group(0) != "")

        def on_validate(P):
            return validate(P)

        def click_quit():
            print("The user clicked 'cancel'")
            self.master.destroy()

        def clear_fields():
            distance_output.delete('1.0', 'end')
            p1lat.set('')
            p1long.set('')
            p2lat.set('')
            p2long.set('')

        def callback():

            # this makes sure the output textbox is clear when the callback function is started
            distance_output.delete('1.0', 'end')

            point1Latitude = ""
            point1Longitude = ""
            point2Latitude = ""
            point2Longitude = ""

            try:

                if  -90 <= float(p1lat.get()) <= 90:
                    point1Latitude = float(p1lat.get())
                else:
                    p1lat.set('Invalid entry')

                if -180 <= float(p1long.get()) <= 180:
                    point1Longitude = float(p1long.get())
                else:
                    p1long.set('Invalid entry')
                    
                if -90 <= float(p2lat.get()) <= 90:
                    point2Latitude = float(p2lat.get())
                else:
                    p2lat.set('Invalid entry')

                if -180 <= float(p2long.get()) <= 180:
                    point2Longitude = float(p2long.get())
                else:
                    p2long.set('Invalid entry')

                if  (-90 <= point1Latitude <= 90 and
                    -180 <= point1Longitude <= 180 and
                    -90 <= point2Latitude <= 90 and
                    -180 <= point2Longitude <= 180 and
                    isinstance(point1Latitude, float) and
                    isinstance(point1Longitude, float) and
                    isinstance(point2Latitude, float) and
                    isinstance(point2Longitude, float)):

                    wgs84_geod = pyproj.Geod(ellps='WGS84')
                    az12, az21, dist = wgs84_geod.inv(point1Longitude, point1Latitude, point2Longitude, point2Latitude)
                    distance_output.insert(tk.INSERT,  dist)
                    print('New set of coordinates')
                    print('The latitude of point 1 is ' + str(point1Latitude))
                    print('The longitude of point 1 is ' + str(point1Longitude))
                    print('The latitude of point 2 is ' + str(point2Latitude))
                    print('The longitude of point 2 is ' + str(point2Longitude))
                    print('The distance between point 1 and point 2 is ' + str(dist) + ' meters.')

                else:
                    
                    return

            except:

                ValueError


        # Title
        title = tk.Label(self, text = "App for finding the distance between two points.", font = title_font)
        # explanation text for GUI
        text1 = tk.Label(self, text="Please enter the latitude (-90 t0 90) and longitude (-180 to 180) of two points.", font = font)
        # explanation text for GUI
        text2 = tk.Label(self, text = "Characters other than the numbers 0 - 9 and . and - will not be accepted.", font = font)
    
        # positioning of title text
        title.grid(row=0, padx=10, pady=10)
        # positioning of two portions of explanatory text
        text1.grid(row=1, padx=10, pady=10)
        text2.grid(row=2, padx=10, pady=10)

        # create frame for entry lables and boxes

        entry_frame = tk.Frame(self)
        entry_frame.grid(row = 3)

        # Labels for input boxes
        label1 = tk.Label(entry_frame, text="Latitude of point 1 (must be between -90 and 90)", font=font)
        label2 = tk.Label(entry_frame, text="Longitude of point 1 (must be between -180 and 180)", font=font)
        label3 = tk.Label(entry_frame, text="Latitude of point 2 (must be between -90 and 90)", font=font)
        label4 = tk.Label(entry_frame, text="Longitude of point 2 (must be between -180 and 180)", font=font)
    
        # The four entryboxes for input, allows floats to deal with lat and long
        # the latitude of point 1
        p1lat_entrybox = tk.Entry(entry_frame, validate="key", textvariable = p1lat)
        vcmd = (p1lat_entrybox.register(on_validate), '%P')
        p1lat_entrybox.config(validatecommand=vcmd)
        # the longitude of point 1
        p1long_entrybox = tk.Entry(entry_frame, validate="key", textvariable = p1long)
        vcmd = (p1long_entrybox.register(on_validate), '%P')
        p1long_entrybox.config(validatecommand=vcmd)
        # the latitude of point 2
        p2lat_entrybox = tk.Entry(entry_frame, validate="key", textvariable = p2lat)
        vcmd = (p2lat_entrybox.register(on_validate), '%P')
        p2lat_entrybox.config(validatecommand=vcmd)
        # the longitude of point 2
        p2long_entrybox = tk.Entry(entry_frame, validate="key", textvariable = p2long)
        vcmd = (p2long_entrybox.register(on_validate), '%P')
        p2long_entrybox.config(validatecommand=vcmd)

        # positioning of input labels and boxes
        label1.grid(row=0, column=0, padx=(20, 0), pady=10)
        p1lat_entrybox.grid(row=0, column=1, padx=(0, 20), pady=10)
        label2.grid(row=1, column=0, padx=(20, 0), pady=10)
        p1long_entrybox.grid(row=1, column=1, padx=(0, 20), pady=10)
        label3.grid(row=2, column=0, padx=(20, 0), pady=10)
        p2lat_entrybox.grid(row=2, column=1, padx=(0, 20), pady=10)
        label4.grid(row=3, column=0, padx=(20, 0), pady=10)
        p2long_entrybox.grid(row=3, column=1, padx=(0, 20), pady=10)
        
        # frame for buttons

        button_frame = tk.Frame(self)
        button_frame.grid(row = 4)

        button1 = tk.Button(button_frame, text="Calculate distance", default='active',
                        command=callback)  # Variables are being attached to callback
        # variables come from the entry boxes and are passed into another function, callback
        button2 = tk.Button(button_frame, text="Cancel", command=click_quit)
        button3 = tk.Button(button_frame, text="Clear fields", command=clear_fields)

        button1.grid(row=0, column=0, sticky='e', padx=20, pady=(5, 10))
        button2.grid(row=0, column=1, sticky='w', padx=20, pady=(5, 10))
        button3.grid(row=0, column=2, sticky='w', padx=20, pady=(5, 10))

        # create a frame for the results boxes

        results_frame = tk.Frame(self)
        results_frame.grid(row = 5)

        # Result label
        result_label1 = tk.Label(results_frame, text="The distance between the two points you entered is: ", font=font)
        result_label2 = tk.Label(results_frame, text=" meters", font=font)
        # box for calculated distance
        distance_output = tk.Text(results_frame, width = 25, height = 1, background = "light grey")


        # positioning the results output label 1
        result_label1.grid(row=0, column=0, padx=(10, 0), pady=10)
        
        # positioning the calculated distance box
        distance_output.grid(row = 0, column = 1)

        # positioning the results output label 2
        result_label2.grid(row=0, column=2, padx=(0, 10), pady=10)


app = Window(root)

root.mainloop()