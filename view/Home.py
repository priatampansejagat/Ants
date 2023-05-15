import tkinter as tk
import time

class Home():

    # receive controllers
    controllers={}


    def __init__(self, controllers):
        controllers = controllers

        # Undefined UI
        global button_remove_rule
        self.button_remove_rule = {}

        global list_rule
        self.list_rule = {}


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
        input_url.grid(row=0, column=1, pady=20, padx=10)

        button = tk.Button(frame_input, text='Dump', width=25, command=lambda:self.data_dump(str(input_url.get())))
        button.grid(row=0, column=2)

        global text_dump
        self.text_dump = tk.Text(frame_input, height=38, width=110, wrap=tk.NONE)
        self.text_dump.grid(row=1,column=0,columnspan=3)

        text_dump_scrollbar_y = tk.Scrollbar(frame_input, command=self.text_dump.yview)
        text_dump_scrollbar_y.grid(row=1, column=3, sticky='nsew')
        self.text_dump['yscrollcommand'] = text_dump_scrollbar_y.set

        text_dump_scrollbar_x = tk.Scrollbar(frame_input, command=self.text_dump.xview, orient='horizontal')
        text_dump_scrollbar_x.grid(row=2, column=0,columnspan=3, sticky='nsew')
        self.text_dump['xscrollcommand'] = text_dump_scrollbar_x.set

        frame_extract = tk.Frame(frame_input, padx=30, pady=15, highlightbackground="grey", highlightthickness=1)
        frame_extract.grid(row=0, column=5, rowspan=2)
        # frame_extract.config(bg="skyblue")

        label_extract_title = tk.Label(frame_extract, text='EXTRACTION LAB', pady=15)
        label_extract_title.grid(row=0, column=0)

        text_grab = tk.Entry(frame_extract, width=40)
        text_grab.grid(row=1, column=0)

        button_add_rule = tk.Button(frame_extract, text='Add Rule', command=lambda:self.add_rules(str(text_grab.get())))
        button_add_rule.grid(row=1, column=1)

        frame_extract_options = tk.Canvas(frame_extract)
        frame_extract_options.grid(row=2, column=0, pady=10,columnspan=2)

        global canvas_extract_options
        self.canvas_extract_options = tk.Canvas(frame_extract_options, width=280, height=480, background='white')
        self.canvas_extract_options.grid(row=0, column=0)

        global rule_items_nest
        self.rule_items_nest=tk.Frame(self.canvas_extract_options,background='white')
        # self.rule_items.grid(row=0,column=0)
        self.canvas_extract_options.create_window((0, 0), window=self.rule_items_nest, anchor='nw')

        global list_rule_scroll
        self.list_rule_scroll = tk.Scrollbar(frame_extract_options,orient="vertical", command=self.canvas_extract_options.yview)
        self.list_rule_scroll.config(command=self.canvas_extract_options.yview)
        self.list_rule_scroll.grid(row=0, column=1, sticky='nsew')
        self.canvas_extract_options['yscrollcommand'] = self.list_rule_scroll.set

        # self.canvas_extract_options.configure(yscrollcommand=list_rule_scroll.set, scrollregion="0 0 0 %s" % self.rule_items_nest.winfo_height())

        frame_button_extraction_action = tk.Frame(frame_extract)
        frame_button_extraction_action.grid(row=3, column=0,columnspan=2)

        button_extraction = tk.Button(frame_button_extraction_action, text='Extract', command=lambda:self.extraction(), background='skyblue')
        button_extraction.grid(row=0, column=1)

        button_clear = tk.Button(frame_button_extraction_action, text='Clear', command=lambda: self.clear_rules_all(), background='pink')
        button_clear.grid(row=0, column=0,padx=5)

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

    def add_rules(self,value='no rules'):
        if len(value.strip(' ')) > 0:
            self.list_rule[str(value)] = tk.Label(self.rule_items_nest, text=str(value),background='white')
            self.list_rule[str(value)].grid(row=len(self.list_rule),column=0)
            # self.list_rule[str(value)].pack()

            # self.button_remove_rule[str(value)] = tk.Button(self.rule_items_nest, text='del', background='red', command=lambda : self.remove_rule(str(value)))
            # self.button_remove_rule[str(value)].grid(row=len(self.list_rule),column=1)

            self.rule_items_nest.update()
            self.canvas_extract_options['scrollregion'] = "0 0 0 %s" % self.rule_items_nest.winfo_height()
        else:
            print('no url')

    """
    def remove_rule(self,value='no url'):
        if len(value.strip(' ')) > 0:
            self.list_rule[str(value)].destroy()
            self.button_remove_rule[str(value)].destroy()
            del self.list_rule[str(value)]
            del self.button_remove_rule[str(value)]

            print('remove {}'.format(self.list_rule))

            self.rule_items_nest.update()
            self.canvas_extract_options['scrollregion'] = "0 0 0 %s" % self.rule_items_nest.winfo_height()
        else:
            print('no url')
    """

    def clear_rules_all(self):
        print('removing all rules')
        if len(self.list_rule) > 0:
            for child in self.rule_items_nest.winfo_children():
                child.destroy()

        else:
            print('No Rules')
            print (self.list_rule)


        self.list_rule.clear()

        self.rule_items_nest.update()
        self.canvas_extract_options['scrollregion'] = "0 0 0 %s" % self.rule_items_nest.winfo_height()

    def extraction(self):
        # for key in self.list_rule:
        #     print(key)
        if len(self.list_rule)>0:
            print('hiolalala')
        else:
            print('Please add rules')




