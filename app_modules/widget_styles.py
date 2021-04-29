app_window_stylesheet = """

#app_window{
    background-color: #121212;
}

"""

title_label_stylesheet = """

#title_label{
    background-color: #232323;
    padding-top: 10px;
    padding-bottom: 10px;
    padding-left: 30px;
    padding-right: 30px;
    
    font-weight: bold; 
    font-family: Verdana; 
    color: #B3B3B3; 
    font-size: 14pt

}
"""

clock_stylesheet = """
#clock{
    background-color: #232323;
    padding-top: 10px;
    padding-bottom: 10px;
    padding-left: 20px;
    padding-right: 20px;
    
    font-weight: bold; 
    font-family: Verdana; 
    color: #1db954; 
    font-size: 11pt
}
"""

task_list_label_stylesheet = """

#task_list_label{
    font-weight: bold; 
    font-family: Verdana; 
    color: #121212; 
    font-size: 11pt
}

"""

task_list_stylesheet = """

#task_list_widget{
    height: 500px; 
    background-color: #282828;
    color: #B3B3B3;
    font-size: 10pt;
    font-weight: bold;
    padding-top: 2px;
    padding-left: 2px;
    padding-bottom: 15px;
    border-radius: 5;
    alternate-background-color: #212121;
}
#task_list_widget::item:hover{
    color: #FFFFFF;
    background: #212121;
}
#task_list_widget::item:selected{
    border: none;
    color: #1db954;
    outline: none;
}
#task_list_widget QScrollBar{
    border: none;
    background: #282828;
    width: 0px
}

"""

add_button_stylesheet = """

#add_button{
    background-color: #282828; 
    font-weight: bold; 
    color: #B3B3B3; 
    border-radius: 10;
}
#add_button::hover{
    background-color: #383838; 
    font-weight: bold; 
    color: #FFFFFF; 
    border-radius: 10;
}

"""

update_button_stylesheet = """

#update_button{
    background-color: #282828; 
    font-weight: bold; 
    color: #B3B3B3; 
    border-radius: 10;
}
#update_button::hover{
    background-color: #383838; 
    font-weight: bold; 
    color: #FFFFFF; 
    border-radius: 10;
}

"""

arch_button_stylesheet = """

#arch_button{
    background-color: #282828; 
    font-weight: bold; 
    color: #B3B3B3; 
    border-radius: 10;
}
#arch_button::hover{
    background-color: #383838; 
    font-weight: bold; 
    color: #FFFFFF; 
    border-radius: 10;
}

"""

task_details_label_stylesheet = """
#task_details_label{
    font-weight: bold; 
    font-family: Verdana; 
    color: #FFFFFF; 
    font-size: 11pt;
}   
"""

task_details_text_stylesheet = """
#task_details_text {
    background-color: #B3B3B3; 
    font-family: Courier;
    padding-top: 5px;
    padding-left: 12px;
    padding-right: 12px;
    font-style: italic; 
    font-size: 12pt;
    border-radius: 5;
}
"""

mot_quote_stylesheet = """

#mot_quote{
    background-color: #800000; 
    color: white; 
    font-weight: bold; 
    font-family: Courier; 
    font-size: 8pt; 
    border: 1px solid black;
}

"""

close_button_stylesheet = """

#close_button{
    background-color: #282828; 
    font-weight: bold; 
    color: #B3B3B3; 
    border-radius: 10;
}
#close_button::hover{
    background-color: #383838; 
    font-weight: bold; 
    color: #FFFFFF; 
    border-radius: 10;
}

"""

dialog_style_sheet = """

#dialog_window{
    background-color: #151617;
}

#task_title_group_box{
    margin-top: 5px;
    padding-bottom: 10px;
    background-color: #3a3b3c;
    border-radius: 10;
}

#task_title_label{
    font-size: 9pt;
    font-weight: bold;
    color: #e4e6eb;
}

#task_title_edit{
    padding-top: 5px;
    padding-bottom: 5px;
    padding-left: 5px;
    background-color: #e4e6eb;
    color: #3a3b3c;
    font-size: 9pt;
    font-weight: bold;
    border-radius: 3;
}

#task_details_group_box{
    margin-top: 10px;
    margin-bottom: 10px;
    padding-bottom: 10px;
    background-color: #3a3b3c;
    border-radius: 10;
    font-size: 10;
    color: #FFFFFF;
}

#task_details_label{
    font-size: 9pt;
    font-weight: bold;
    color: #e4e6eb;
}

#task_details_edit{
    padding-top: 5px;
    padding-bottom: 5px;
    background-color: #e4e6eb;
    color: #3a3b3c;
    font-weight: bold;
    font-size: 9pt;
}

#save_button{
    width: 100px;
    height: 30px;
    background-color: #282828; 
    font-weight: bold; 
    color: #B3B3B3; 
    border-radius: 10;
}

#save_button::hover{
    background-color: #383838; 
    font-weight: bold; 
    color: #FFFFFF; 
    border-radius: 10;

}

#cancel_button{
    height: 30px;
    background-color: #282828; 
    font-weight: bold; 
    color: #B3B3B3; 
    border-radius: 10;
}

#cancel_button::hover{
    background-color: #383838; 
    font-weight: bold; 
    color: #FFFFFF; 
    border-radius: 10;

}

"""
