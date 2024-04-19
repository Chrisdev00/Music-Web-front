import reflex as rx
import Music_Web.styles.styles as styles
from Music_Web.styles.fonts import FontWeight
from Music_Web.components.sidebar_status import State


def sidebar():

    return rx.grid(                                                                # class sidebar
            rx.box(                                                                     # class logo
                rx.button(                                                              # class menu-btn
                    rx.lucide.icon(
                        tag="log-out"
                    ),
                    display=["none", "flex", "flex", "none", "none"],
                    margin_top="14px",                                                    
                    class_name="container-main-header-navlinks-sidebar-logo-button",
                ),
                rx.lucide.icon(                                                         # i
                    tag = "activity",
                    color = "#fff",
                    cursor = "pointer",
                    font_size = "24px",
                    transition = "all 0.3s ease",
                    margin_top="14px",
                    _hover = {"color": "#5773ff"}
                ),                
                rx.link(                                                                # link a
                    "AsmrProg", 
                    font_weight = FontWeight.BOLD.value,
                    transition = "all 0.3s ease",
                    text_decoration = "none",
                    color = "#fff",
                    margin_top="14px",
                    _hover = {"color": "#5773ff"}

                ), 
                style=styles.logo_style               
            ),            
            rx.box(                                                                     # class menu
                rx.text(                                                                # h5
                    "Menu",
                    style=styles.h5_style
                ),                                
                rx.list(                                                                # ul
                    rx.hstack(                                                       # li
                        rx.link(
                            rx.lucide.icon(tag="zap", class_name="icon-class"),    # i
                            "Explore",
                            style=styles.link_style                                                                      
                        ),
                        href="",                        
                        style=styles.li_style,                 
                    ),                    
                    rx.hstack(                                                       # li
                        rx.link(                                                        # link a
                            rx.lucide.icon(tag="volume-2", class_name="icon-class"),        # i
                            "Genres",                            
                            style=styles.link_style
                        ),
                        style=styles.li_style
                    ),
                    rx.hstack(                                                       # li
                        rx.link(                                                        # link a
                            rx.lucide.icon(tag="book-image", class_name="icon-class"),      # i
                            "Albums",
                            style=styles.link_style                                                          
                        ),
                        style=styles.li_style       
                    ),
                    rx.hstack(                                                       # li
                        rx.link(                                                        # link a
                            rx.lucide.icon(tag="mic", class_name="icon-class"),             # i
                            "Artists",
                            style=styles.link_style
                        ),
                        style=styles.li_style
                    ),                    
                    rx.hstack(                                                       # li
                        rx.link(                                                        # link a
                            rx.lucide.icon(tag="radio", class_name="icon-class"),           # i
                            "Poddcasts",
                            style=styles.link_style
                        ),
                        style=styles.li_style
                    ),
                    style=styles.ul_style,
                         
                ),
            ),
            rx.box(                                                                     # class menu
                rx.text(                                                                # h5
                    "Library",
                    style=styles.h5_style
                ),                                
                rx.list(                                                                # ul
                    rx.hstack(                                                          # li
                        rx.link(                                                        # link a
                            rx.lucide.icon(tag="undo-2", class_name="icon-class"),          # i
                            "Recent",
                            style=styles.link_style
                        ),
                        style=styles.li_style                                            
                    ),                    
                    rx.hstack(                                                       # li
                        rx.link(                                                        # link a
                            rx.lucide.icon(tag="album", class_name="icon-class"),           # i
                            "Albums",
                            style=styles.link_style
                        ),
                        style=styles.li_style
                    ),
                    rx.hstack(                                                       # li
                        rx.link(                                                        # link a
                            rx.lucide.icon(tag="heart", class_name="icon-class"),           # i
                            "Favourites",
                            style=styles.link_style                                                           
                        ),
                        style=styles.li_style       
                    ),
                    rx.hstack(                                                       # li
                        rx.link(                                                        # link a
                            rx.lucide.icon(tag="folder-open", class_name="icon-class"),     # i
                            "Local",
                            style=styles.link_style
                        ),
                        style=styles.li_style
                    ),         
                    style=styles.ul_style       
                ),
            ),
            rx.box(                                                                     # class menu
                rx.text(                                                                # h5
                    "Playlist",
                    style=styles.h5_style
                ),                                
                rx.list(                                                                # ul
                    rx.hstack(                                                       # li
                        rx.link(                                                        # link a
                            rx.lucide.icon(tag="plus-square", class_name="icon-class"),     # i
                            "Create New",
                            style=styles.link_style
                        ),
                        style=styles.li_style                                           
                    ),                    
                    rx.hstack(                                                       # li
                        rx.link(                                                        # link a
                            rx.lucide.icon(tag="play-circle", class_name="icon-class"),     # i
                            "Best of 2023",
                            style=styles.link_style
                        ),
                        style=styles.li_style
                    ),
                    rx.hstack(                                                       # li
                        rx.link(                                                        # link a
                            rx.lucide.icon(tag="play-circle", class_name="icon-class"),     # i
                            "Best of 2022",
                            style=styles.link_style                                                           
                        ),
                        style=styles.li_style      
                    ),
                    rx.hstack(                                                       # li
                        rx.link(                                                        # link a
                            rx.lucide.icon(tag="play-circle", class_name="icon-class"),     # i
                            "Kael Fischer",
                            style=styles.link_style
                        ),
                        style=styles.li_style
                    ),                    
                    style=styles.ul_style        
                ),
            ),

            rx.box(                                                                 # class playing
                rx.box(                                                             # class top
                    rx.image(                                                       # img
                        src="/current.png", 
                        style=styles.image_style,
                        width = "36px",
                        height = "36px"
                    ),                         
                    rx.text("Apple Homepod"),                                       # h4
                    style=styles.playing_top_style
                ),
                rx.box(                                                             # class bottom
                    rx.lucide.icon(tag="podcast", class_name="icon-class"),         # i
                    rx.text(                                                                               # p
                        "Playing on Device",
                        class_name="sidebar-playing-bottom-p"                        
                    ),
                    style=styles.playing_bottom_style                
                ),
                margin_right="40px",
                width="100%",                
            ),
            class_name="container-sidebar",
            style=styles.sidebar_style,
            # col_start= 1,
            # col_span= 1,
            visible=State.sidebar_visible,

        )