import reflex as rx
import Music_Web.styles.styles as styles




def main_container ():

    return rx.grid(                                                   # etiqueta main
        rx.box(                                                      # etiqueta header
           rx.box(                                                   # class nav-links
               rx.button(
                   rx.lucide.icon(
                       tag="menu"
                   ),                   
                   #on_click=State.toggle_sidebar,
                   display=["none", "flex", "flex", "none", "none"],                   
                   class_name="container-main-header-navlinks-sidebar-logo-button",
                   style=styles.container_main_header_navlinks_sidebar_logo_button,
                   
               ),
               rx.link(                                                     # a
                   "Music", 
                   style=styles.navlinks_a, 
                   class_name="main-header-navlinks-a"
                ),                                  
               rx.link(
                   "Live", 
                   style=styles.navlinks_a, 
                   class_name="main-header-navlinks-a"
                ),
               rx.link(
                   "Podcast", 
                   style=styles.navlinks_a, 
                   class_name="main-header-navlinks-a"
                ),
               style=styles.navlinks_style
           ),
           rx.hstack(                                                   # class search
                rx.icon(tag="search", class_name="icon-class", style=styles.icon_style),
                rx.input(
                    placeholder='Type here to search',
                    width= "100%",
                    background_color= "transparent",
                    border = "none",
                    outline = "none",
                    class_name="main-header-search-input"
                    #color = "#fff"
                ),
                style=styles.search_style,             
                class_name="main-header-search",
            ),
            style=styles.main_header_style
        ),
        rx.box(                                                       # Etiqueta trending
            rx.box(                                                   # class left
                rx.heading("Trending New Song", size="3"),                      # h5
                rx.box(                                               # class info
                    rx.text("Lost Emotions", class_name="main-trending-left-info-h2", margin_bottom="8px"),     # h2
                    rx.text("Rion Clarke", display="inline"),                        # h4
                    rx.text(                                          # h5
                        "63 Million Plays", 
                        class_name="main-trending-left-info-h5",                        
                    ),                   
                    rx.box(                                           # buttons
                        rx.button(
                            "Listen Now",                            
                            style=styles.trending_button,
                            class_name="main-trending-left-info-buttons-button",
                        ),
                        rx.icon(
                            tag="view",
                            class_name="main-trending-left-info-buttons-i",
                            style=styles.trending_buttons_icon,
                        ),
                        style=styles.trending_buttons
                    ),
                    margin_top = "12px",
                    padding = "26px"
                ),
            ),
            rx.image(
                src="/trend.png",
                class_name="main-trending-img",
            ),
            class_name="main-trending",
            style=styles.trending_style,

        ),
        rx.box(                                                         # class playlist
            rx.box(                                                     # class genres
                rx.box(                                                 # class header
                    rx.text("Genres"),                                  # h5
                    rx.link("See all", style=styles.genres_music_list_a),    # a
                    style=styles.genres_music_list_header_2
                ),
                rx.box(                                                 # class items
                    rx.box(                                          # class item
                        rx.text("Electro", class_name="main-playlist-genres-items-item-p"),
                        rx.text("Pop", class_name="main-playlist-genres-items-item-p"),
                        style=styles.genres_items_item,
                        background_color= "#476a8a",
                        class_name="main-playlist-genres-items-item"                        
                    ),
                    rx.box(                                          # class item
                        rx.text("Dance", class_name="main-playlist-genres-items-item-p"),
                        rx.text("Beat", class_name="main-playlist-genres-items-item-p"),
                        style=styles.genres_items_item,
                        background_color= "#a69984",
                        class_name="main-playlist-genres-items-item"                      
                    ),
                    rx.box(                                          # class item
                        rx.text("ClubHouse", class_name="main-playlist-genres-items-item-p"),
                        rx.text("Remix", class_name="main-playlist-genres-items-item-p"),
                        style=styles.genres_items_item,
                        background_color= "#a24c34",
                        class_name="main-playlist-genres-items-item"                      
                    ),
                    rx.box(                                          # class item
                        rx.text("Hip Hop", class_name="main-playlist-genres-items-item-p"),
                        rx.text("Rap", class_name="main-playlist-genres-items-item-p"),
                        style=styles.genres_items_item,
                        background_color= "#0d4045",
                        class_name="main-playlist-genres-items-item"                       
                    ),
                    rx.box(                                          # class item
                        rx.text("Alternative", class_name="main-playlist-genres-items-item-p"),
                        rx.text("Indie", class_name="main-playlist-genres-items-item-p"),
                        style=styles.genres_items_item,
                        background_color= "#a67894",
                        class_name="main-playlist-genres-items-item"                        
                    ),
                    rx.box(                                          # class item
                        rx.text("Classical", class_name="main-playlist-genres-items-item-p"),
                        rx.text("Period", class_name="main-playlist-genres-items-item-p"),
                        #style=styles.genres_items_item,
                        background_color= "#5547a5",
                        class_name="main-playlist-genres-items-item-child-6"                       
                    ),                    
                    display = "grid",                    
                    gap = "10px",
                    class_name="main-playlist-genres-items",
                ),
                style=styles.playlist_genres,
                class_name="main-playlist-genres"
            ),
            rx.box(                                                  # class music-List
                rx.box(                                              # class header
                    rx.text("Top Songs"),                            # h5
                    rx.link("See all", style=styles.genres_music_list_a),      # a
                    style=styles.genres_music_list_header_2
                ),
                rx.box(                                              # items
                    rx.box(                                          # item
                        rx.box(                                      # info
                            rx.text("01", style=styles.music_list_items_item_info_actions_p, class_name="main-playlist-music-list-items-item-info-p"),                           # p
                            rx.image(src="/song-1.png", width= "50px", height="50px"),
                            rx.box(                                  # class details
                                rx.text("Sunrise"),                  # h5
                                rx.text("Lila Rivera", style=styles.music_list_items_item_info_actions_p)               # p
                            ),
                            style=styles.music_list_items_item_info_actions
                        ),
                        rx.box(                                      # class actions
                            rx.text("03:45", font_size="13px", font_weight="bold"),           # p
                            rx.box(                                  # class icon
                                rx.lucide.icon(tag="play", class_name="icon-class", width="12px", height="12px", color="#5773ff"),
                                style=styles.music_list_items_item_actions_icon
                            ),
                            rx.lucide.icon(tag="plus-square", class_name="icon-class", color="#919191"),
                            style=styles.music_list_items_item_info_actions
                        ),
                        style=styles.music_list_items_item
                    ),
                    rx.box(                                          # item
                        rx.box(                                      # info
                            rx.text("02", style=styles.music_list_items_item_info_actions_p, class_name="main-playlist-music-list-items-item-info-p"),                           # p
                            rx.image(src="/song-2.png", width= "50px", height="50px"),
                            rx.box(                                  # class details
                                rx.text("Voyage"),                  # h5
                                rx.text("Tyde Brennan", style=styles.music_list_items_item_info_actions_p)               # p
                            ),
                            style=styles.music_list_items_item_info_actions
                        ),
                        rx.box(                                      # class actions
                            rx.text("04:30", font_size="13px", font_weight="bold"),           # p
                            rx.box(                                  # class icon
                                rx.lucide.icon(tag="play", class_name="icon-class", width="12px", height="12px", color="#5773ff"),
                                style=styles.music_list_items_item_actions_icon
                            ),
                            rx.lucide.icon(tag="plus-square", class_name="icon-class", color="#919191"),
                            style=styles.music_list_items_item_info_actions
                        ),
                        style=styles.music_list_items_item
                    ),
                    rx.box(                                          # item
                        rx.box(                                      # info
                            rx.text("03", style=styles.music_list_items_item_info_actions_p, class_name="main-playlist-music-list-items-item-info-p"),                           # p
                            rx.image(src="/song-3.png", width= "50px", height="50px"),
                            rx.box(                                  # class details
                                rx.text("Breeze"),                  # h5
                                rx.text("Sola Kim", style=styles.music_list_items_item_info_actions_p)               # p
                            ),
                            style=styles.music_list_items_item_info_actions
                        ),
                        rx.box(                                      # class actions
                            rx.text("04:22", font_size="13px", font_weight="bold"),           # p
                            rx.box(                                  # class icon
                                rx.lucide.icon(tag="play", class_name="icon-class", width="12px", height="12px", color="#5773ff"),
                                style=styles.music_list_items_item_actions_icon
                            ),
                            rx.lucide.icon(tag="plus-square", class_name="icon-class", color="#919191"),
                            style=styles.music_list_items_item_info_actions
                        ),
                        style=styles.music_list_items_item
                    ),
                    rx.box(                                          # item
                        rx.box(                                      # info
                            rx.text("04", style=styles.music_list_items_item_info_actions_p, class_name="main-playlist-music-list-items-item-info-p"),                           # p
                            rx.image(src="/song-4.png", width= "50px", height="50px"),
                            rx.box(                                  # class details
                                rx.text("Twilight"),                  # h5
                                rx.text("Jett Lawsonn", style=styles.music_list_items_item_info_actions_p)               # p
                            ),
                            style=styles.music_list_items_item_info_actions
                        ),
                        rx.box(                                      # class actions
                            rx.text("03:17", font_size="13px", font_weight="bold"),           # p
                            rx.box(                                  # class icon
                                rx.lucide.icon(tag="play", class_name="icon-class", width="12px", height="12px", color="#5773ff"),
                                style=styles.music_list_items_item_actions_icon
                            ),
                            rx.lucide.icon(tag="plus-square", class_name="icon-class", color="#919191"),
                            style=styles.music_list_items_item_info_actions
                        ),
                        style=styles.music_list_items_item
                    ),
                ),
                class_name="main-playlist-music-list",
                style=styles.playlist_music_List
            ),
            class_name="main-playlist"
        ),
        # col_start=2,
        # col_span=1,        
        style=styles.main_style,
        #class_name="main"
    )