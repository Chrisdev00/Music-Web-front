import reflex as rx
import Music_Web.styles.styles as styles


def right_section ():
    
    return rx.box(                                      # class right-section
        rx.box(                                              # class profile
            rx.lucide.icon(tag="bell", class_name="icon-class", color="#fff"),                         # i
            rx.lucide.icon(tag="settings", class_name="icon-class", color="#fff"),                     # i
            rx.box(                                             # user
                rx.box(                                         # left
                    rx.image(
                        src="/profile.png", 
                        width="30px", 
                        height="30px"
                    ),
                    style=styles.right_section_profile_user_left
                ),
                rx.box(                                         # right
                    rx.text("Jhon Doe"),                        # h5
                    style=styles.right_section_profile_user_right
                ),
                display="flex"
            ),
            class_name="right-section-profile",
            style=styles.right_section_profile
        ),
        rx.box(                                                 # music-player
            rx.box(                                             # top-section
                rx.box(                                         # header
                    rx.text("Player"),                          # h5
                    rx.lucide.icon(tag="list-music", class_name="icon-class"),           # i
                    style=styles.right_section_music_player_header
                ),
                rx.box(                                         # song-info
                    rx.image(                                   # img
                        src="/player.png",
                        class_name="right-section-music-player-song-info-img",
                        #width="280px",
                        #height="220px"
                    ),                
                    rx.box(                                     # description
                        rx.text(                                # h3
                            "Ripple Echoes",
                            class_name="right-section-music-player-song-info-description-h3",
                            #font_size="26px",
                            #font_weight="500",
                            #margin_bottom="8px"
                        ),               
                        rx.text(                                # h5
                            "Kael Fisher",
                            font_size= "16px",
                            margin_bottom= "4px"
                        ),                 
                        rx.text(                                # p
                            "Best of 2024",
                            color = "#919191",
                            font_size = "12px",
                            font_weight= "bold"
                        ),               
                    ),
                    rx.box(                                     # progress
                        rx.text("02:45", font_size="11px"),     # p
                        rx.box(                                # active-line
                            #style=styles.song_info_progress_active_line,
                            class_name="active-line-before"
                        ),                               
                        rx.box(                                 # deactive-line
                            class_name="right-section-music-player-song-info-progress-deactive-line",
                            style=styles.song_info_progress_deactive_line
                        ),                               
                        rx.text("01:02", font_size="11px"),
                        class_name="right-section-music-player-song-info-progress",
                        style=styles.song_info_progress
                    ),
                    style=styles.right_section_music_player_song_info
                ),
                padding="20px",
                height="86%"
            ),
            rx.box(                                             # player-actions
                rx.hstack(                                      # buttons
                    rx.lucide.icon(tag="repeat", class_name="icon-class"),               # i
                    rx.lucide.icon(tag="chevron-first", class_name="icon-class"),
                    rx.lucide.icon(
                        tag="play",
                        class_name="right-section-music-player-player-actions-buttons-play-button",
                        width="3rem",
                        height="3rem",
                        #class_name="icon-class", 
                        #padding="9px",
                        color = "#5773ff",
                        background_color="#fff",
                        #border_radius = "8px"
                    ),
                    rx.lucide.icon(tag="chevron-last", class_name="icon-class"),
                    rx.lucide.icon(tag="arrow-right-left", class_name="icon-class"),
                    class_name="right-section-music-player-player-actions-buttons",
                    style=styles.right_section_music_player_player_actions_buttons
                ),
                rx.box(                                                                  # lyrics
                    rx.lucide.icon(tag="chevron-up", class_name="icon-class"),           # i
                    rx.text("LYRICS"),                                                   # h5
                    style=styles.player_actions_lyrics
                ),
                style=styles.right_section_music_player_player_actions
            ),
            class_name="right-section-music-player",
            style=styles.right_section_music_player
        ),
        class_name="right-section"
    )