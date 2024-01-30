import webview
import webbrowser

class Api:

    def __init__(self):
        self._window = None

    def set_window(self):
        self._window = window

    def destroy(self):
        # print('Destroying window..')
        window.destroy()
        # print('Destroyed!')

    def timemoto(self):
        webbrowser.register('firefox',
                            None,
                            webbrowser.BackgroundBrowser("C://Program Files//Mozilla Firefox//firefox.exe"))

        webbrowser.get('firefox').open('https://app.timemoto.com/Account/Login?ReturnUrl=%2FUserSetting%2FEdit%2Fb6122f67018447a6af48695f60fc092b')

    def trello(self):
        webbrowser.register('firefox',
                            None,
                            webbrowser.BackgroundBrowser("C://Program Files//Mozilla Firefox//firefox.exe"))
        webbrowser.get('firefox').open('https://trello.com/de/login')
    
    def emby(self):
        webbrowser.register('firefox',
                            None,
                            webbrowser.BackgroundBrowser("C://Program Files//Mozilla Firefox//firefox.exe"))
        webbrowser.get('firefox').open('http://emby.tce.lan:8096/web/index.html#!/startup/login.html?serverId=0ef980adca5b414abc81c461f639690a')

    def outlook(self):
        webbrowser.register('firefox',
                            None,
                            webbrowser.BackgroundBrowser("C://Program Files//Mozilla Firefox//firefox.exe"))
        webbrowser.get('firefox').open('https://login.live.com/')

if __name__ == '__main__':
    api = Api()
    window = webview.create_window('TCE Launcher V2', 'home.html',
                                   width=1100, height=850, resizable=False, confirm_close=True, js_api=api)
    webview.start()
