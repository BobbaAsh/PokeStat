html_layout = '''<!DOCTYPE html>
                    <html>
                        <head>
                            {%metas%}
                            <title>PokeCompare</title>
                            {%favicon%}
                            {%css%}
                        </head>
                        <body class="dash-template">
                            <header>
                              <div class="nav-wrapper">
                                <a href="/">
                                    <img src="/static/img/logo.png" class="logo" />
                                    <h1>PokeStat</h1>
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
