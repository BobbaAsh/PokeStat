html_layout = '''<!DOCTYPE html>
                    <html>
                        <head>
                            {%metas%}
                            <title>GameData</title>
                            {%favicon%}
                            {%css%}
                        </head>
                        <body class="dash-template">
                            <header>
                              <div class="nav-wrapper">
                                <a href="/">
                                    <img src="/static/img/favicon.png" class="logo" />
                                    <h1>Gamedata</h1>
                                  </a>
                                <nav>
                                </nav>
                            </div>
                            </header>
                            {%app_entry%}
                            <footer>
                                {%config%}
                                {%scripts%}
                                {%renderer%}
                            </footer>
                        </body>
                    </html>'''
