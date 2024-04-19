

STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Roboto:wght@300;500&display=swap",
    "https://fonts.googleapis.com/css2?family=Comfortaa:wght@500&display=swap"
]

# class State(rx.State):
#     sidebar_visible: bool = False

#     def toogle_sidebar(self):
#         self.sidebar_visible = not self.sidebar_visible,
        


link_style = {
    "display":"flex",
    "direction":"row",
    "gap":"20px",                        # a
    "text_decoration": "none",
    "color": "#fff",
    "_hover" : {"color": "#5773ff"},
    "font_size": "14px",
    "font_weight": "medium",
    "transition": "all 0.3s ease"
}

icon_style = {                       # i
    "color": "#fff",
    "cursor": "pointer"
}

image_style = {                      # img
    "object_fit": "cover",
    "object_position": "top",
    "border_radius": "8px"
}

container_style = {
    "width" : "100%",
    "display": "grid",    
    "grid_template_columns": "1fr 4fr 2fr",
    "background": "linear-gradient(#050505, #18181d)" 
}

sidebar_style = {
    "height": "100vh",    
    "background_color": "#18181d",
    "padding": "20px 36px",
    #"position": "fixed",
    #"left": "0",   
    "display": "flex",
    "flex_direction": "column",
    "justify_content": "space-between",
    "z-index": "1000",
    "transition": "all 0.6s ease",
}

logo_style = {
    "display": "flex",
    "align_items": "center",
    "gap": "6px"
}

h5_style = {
    "color" : "#919191",
    "margin_bottom" : "12px",
    "text_transform" : "uppercase"
}

ul_style = {
    "list_style": "none"
}

li_style = {
    "margin_bottom": "12px",
    "display": "flex",
    "align_items": "center",    
    "gap": "20px",
    "cursor": "pointer",    
}

playing_top_style = {
    "background_color": "#32323d",
    "border_radius": "6px 6px 0 0",
    "padding": "10px",
    "display": "flex",
    "align_items": "center",
    "gap": "10px",
    "color": "#fff",
    "font_size": "13px"
}

playing_top_style_img = {
    "width": "36px",
    "height": "36px"
}

playing_bottom_style = {
    "background_color": "#25252d",
    "border_radius": "0 0 6px 6px",
    "padding": "8px",
    "display": "flex",
    "align_items": "center",
    "justify_content": "center",
    "gap": "6px",
    "font_size": "12px",
}

#######  Estilos de la etiqueta Main #######

main_style = {
    "padding": "20px 36px"    
}

main_header_style = {
    "display": "flex",
    "align_items": "center",
    "justify_content": "space-between"
}

navlinks_style = {
    "display": "flex",
    "align_items": "center",
    "gap": "20px"
}

navlinks_a = {
    "text_transform": "uppercase",
    "color": "#919191",
    "transition": "all 0.3s ease",
    "_hover" : {"color": "#5773ff"}
}

search_style = {
    "display": "flex",
    "align_items": "center",
    "gap": "6px",
    #"width": "70%",
    "background_color": "#1d1d1d",
    "border": "1px solid #464748",
    "padding": "10px",
    "border_radius": "8px"
}

trending_style = {
    "margin_top": "40px",
    #"display": "flex",
    "align_items": "center",
    "justify_content": "space-between",
    "color": "#fff",
}

trending_buttons = {
    "margin_top": "30px",
    "display": "flex",
    "align_items": "center",
    "gap": "16px",
    "cursor": "pointer"   
}

trending_button = {
    # "padding": "12px 16px",
    "background_color": "#5773ff",
    "border": "none",
    "border_radius": "14px",
    "color": "#fff",
    "font_weight": "regular",
    "cursor": "pointer",  
    "_hover" : {"backgroun-color": "#5773ff"}    
}

trending_buttons_icon = {
    "color": "#5773ff",
    #"font_size": "36px",
    "border": "1px solid #fff",
    "padding": "5px",
    "border_radius": "50%"
}

playlist_genres = {
    "color": "#fff",
    "background_color": "#202026",
    "padding": "20px",
    "border_radius": "6px",
    #"width": "40%"
}

genres_music_list_header_2 = {
    "display": "flex",
    "align_items": "center",
    "justify_content": "space-between",
    "margin_bottom": "30px",
}

genres_music_list_a = {
    "color": "#919191",
    "font_size": "12px"
}

genres_items_item = {
    #"padding": "22px 10px",    
    "display": "flex",    
    "justify_content": "center",
    "border_radius": "6px",
    "cursor": "pointer",
    "flex_direction": "column",
    "font_size":"14px", 
    "font_weight":"bold",    
    "flex_wrap": "wrap",
    "align_content": "center"    
}

playlist_music_List = {
    "background_color": "#202026",
    "padding": "20px",
    "color": "#fff",
    "border_radius": "6px",
    #"width": "65%"
}

music_list_items_item = {
    "display": "flex",
    "align_items": "center",
    "justify_content": "space-between",
    "margin_bottom": "20px"
}

music_list_items_item_info_actions = {
    "display": "flex",
    "align_items": "center",
    "gap": "20px"
}

music_list_items_item_info_actions_p = {
    "color": "#919191",
    "font_size": "12px",
    #"font_weight": "bold",
    "margin_top": "6px"
}

music_list_items_item_actions_icon = {
    "display": "flex",
    "align_items": "center",
    "justify_content": "center",
    "background_color": "#32323d",
    "padding": "6px",
    "border": "2px solid #464748",
    "border_radius": "6px"
}


########  Estilos right side  ##########

right_section_profile = {
    "display": "flex",
    "align_items": "center",
    #"justify_content": "flex-end",
    "gap": "18px",
    #"margin_bottom": "40px"
}

right_section_profile_user_left = {
    "display": "flex",
    "align_items": "center",
    "background": "#32323d",
    "padding": "6px",
    "border_radius": "6px 0 0 6px"
}

right_section_profile_user_right = {
    "background_color": "#25252d",
    "border_radius": "0 6px 6px 0",
    "padding": "13px",
    "color": "#fff"
}

right_section_music_player = {
    #"color": "#fff",
    "background_color": "#202026",
    "border_radius": "6px",
    #"height": "88%",
    "display": "flex",
    "flex_direction": "column"
}

right_section_music_player_header = {
    "display": "flex",
    "align_items": "center",
    "justify_content": "space-between",
    "margin_bottom": "30px"
}

right_section_music_player_song_info = {
    "display": "flex",
    "flex-direction": "column",
    "align-items": "center",
    "gap": "24px",
    "text-align": "center"
}

song_info_progress = {
    "display": "flex",
    "align_items": "center",
    #"margin": "10px 0"
}

song_info_progress_active_line = {
    "position": "relative",
    "width": "120px",
    "height": "2px",
    "background_color":"#fff",
    "margin_left": "30px"
}

song_info_progress_deactive_line = {
    #"width": "80px",
    "height": "2px",
    "background_color": "#919191",
    "margin_right": "30px"
}

right_section_music_player_player_actions = {
    "background_color": "#5773ff",
    "height": "26%",
    "border_radius": "6px",
    "display": "flex",
    "flex_direction": "column",
    "align_items": "center",
    "position": "relative"
}

right_section_music_player_player_actions_buttons = {
    "display": "flex",
    "align_items": "center",
    "gap": "30px",
    #"margin_top": "24px"
    "justify_content": "center"
}

player_actions_lyrics = {
    "display": "flex",
    "flex_direction": "column",
    "align_items": "center",
    "position": "absolute",
    "bottom": "8px"
}

container_main_header_navlinks_sidebar_logo_button = {
    "align_items": "center",
    "justify_content": "center",
    "background_color": "#1d1d1d",
    "border": "1px solid #464748",
    "font_size": "20px",
    "padding": "4px",
    "border_radius": "8px",
    "cursor": "pointer",    
}