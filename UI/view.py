import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.DARK
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.dd_year = None
        self.dd_retailer = None
        self.dd_brand = None
        self.btn_topSales = None
        self.btn_analise = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        # title
        self._title = ft.Text("Analizza Vendite", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW 1
        # dropdown for the year, brand and retailer
        self.dd_year = ft.Dropdown(
            label="anno",
            width=150,
            options=[],
            on_click=self._controller.leggi_anno
        )

        self.dd_brand = ft.Dropdown(
            label="brand",
            width=200,
            options=[],
            on_click=self._controller.leggi_brand
        )

        self.dd_retailer = ft.Dropdown(
            label="retailer",
            width=250,
            options=[],
            on_click=self._controller.leggi_retailer
        )

        # populate dropdown
        self._controller.populate_dd_year()
        self._controller.populate_dd_brand()
        self._controller.populate_dd_retailer()

        row1 = ft.Row([self.dd_year, self.dd_brand, self.dd_retailer],
                      alignment=ft.MainAxisAlignment.START)
        self._page.controls.append(row1)


        # ROW 2
        # buttons for the "top Vendite" and "Analizza vendite" display
        self.btn_topSales = ft.ElevatedButton(text="Top Vendite", on_click=self._controller.handle_topSales)
        self.btn_analise = ft.ElevatedButton(text="Analizza Vendite", on_click=self._controller.handle_analise)

        row2 = ft.Row([self.btn_topSales, self.btn_analise],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
