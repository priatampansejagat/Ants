import tkinter as tk

class Home():

    # receive controllers
    controllers={}


    def __init__(self, controllers):
        controllers = controllers

        # CREATE UI
        main_window = tk.Tk(screenName='main_screen', baseName='main_basename', className='Ants', useTk=1)
        main_window.title('Ants')
        main_window.geometry('{}x{}'.format(1300,720))

        container = tk.Frame(main_window, height=720, width=1300)
        container.pack(side="top", fill="both", expand=True)
        # container.config(bg="skyblue")

        frame_input = tk.Frame(container, padx=10, pady=5)
        frame_input.grid(row=0, column=0)

        label_url = tk.Label(frame_input, text='URL')
        # label_url.pack(side='left',fill='both')
        label_url.grid(row=0, column=0)

        input_url = tk.Entry(frame_input, width=100)
        input_url.grid(row=0, column=1, pady=10, padx=10)

        button = tk.Button(frame_input, text='Dump', width=25, command=lambda:self.data_dump(str(input_url.get())))
        button.grid(row=0, column=2)

        global text_dump
        self.text_dump = tk.Text(frame_input, height=40, width=110)
        self.text_dump.grid(row=1,column=0,columnspan=3,pady=10)

        text_dump_scrollbar = tk.Scrollbar(frame_input, command=self.text_dump.yview)
        text_dump_scrollbar.grid(row=1, column=3, sticky='nsew')
        self.text_dump['yscrollcommand'] = text_dump_scrollbar.set

        frame_extract = tk.Frame(frame_input, padx=30, pady=15, highlightbackground="grey", highlightthickness=1)
        frame_extract.grid(row=0, column=5, rowspan=2)
        # frame_extract.config(bg="skyblue")

        label_extract_title = tk.Label(frame_extract, text='EXTRACTION LAB', pady=15)
        label_extract_title.grid(row=0, column=0)

        text_grab = tk.Entry(frame_extract, width=40)
        text_grab.grid(row=1, column=0)

        button_grab_data = tk.Button(frame_extract, text='Add Rule', command=lambda:self.grab_data(str(text_grab.get())))
        button_grab_data.grid(row=1, column=1)


        frame_extract_options = tk.Frame(frame_extract)
        frame_extract_options.grid(row=2, column=0)

        """
        tinggal tambah list rule sama tombol execute extract
        """

        menu = tk.Menu(main_window)
        main_window.config(menu=menu)

        filemenu = tk.Menu(menu)
        menu.add_cascade(label='File', menu=filemenu)
        filemenu.add_command(label='Exit', command=main_window.quit)

        main_window.mainloop()

        pass


    # Initiate function
    def data_dump(self,value='no url'):
        if len(value.strip(' ')) > 0:
            print(value)
        else:
            print('no url')

    def grab_data(self,value='no url'):
        if len(value.strip(' ')) > 0:
            print(value)
        else:
            print('no url')

    def remove_datagrab(self,value='no url'):
        if len(value.strip(' ')) > 0:
            print(value)
        else:
            print('no url')









#  UI DESIGN
class UI(tk.Tk):

    def __init__(self, *args, **kwargs):



        pass


