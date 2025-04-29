import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self.retailer_selezionato = None
        self.brand_selezionato = None
        self.anno_selezionato = None
        self.retailer = None
        self.brand = None
        self.year = None
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_topSales(self, e):
        if self.anno_selezionato is None:
            self._view.create_alert("anno non selezionato!")
            return
        if self.brand_selezionato is None:
            self._view.create_alert("brand non selezionato!")
            return
        if self.retailer_selezionato is None:
            self._view.create_alert("retailer non selezionato!")
            return
        elencoVendite = self._model.get_sales(self.anno_selezionato, self.brand_selezionato, self.retailer_selezionato)
        if len(elencoVendite) == 0:
            self._view.txt_result.controls.append(ft.Text("Nessuna vendita presente"))
        else:
            for v in elencoVendite:
                self._view.txt_result.controls.append(ft.Text(v.__str__()))



        self._view.update_page()

    def handle_analise (self, e):
        pass

    def leggi_anno (self, e):
        self.anno_selezionato = e.control.value

    def leggi_brand (self, e):
        self.brand_selezionato = e.control.value

    def leggi_retailer (self, e):
        self.retailer_selezionato = e.control.value

    def populate_dd_year(self):
        anni = self._model.get_anni()
        for year in anni:
            self._view.dd_year.options.append(ft.dropdown.Option(key=year, text=year,
                                                                 data=year))
        self._view.dd_year.on_change = self.leggi_anno
        self._view.update_page()

    def populate_dd_brand(self):
        brand = self._model.get_brand()
        for b in brand:
            self._view.dd_brand.options.append(ft.dropdown.Option(key=b, text=b,
                                                                 data=b))
        self._view.dd_brand.on_change = self.leggi_brand
        self._view.update_page()

    def populate_dd_retailer(self):
        retailer = self._model.get_retailer()
        for r in retailer:
            self._view.dd_retailer.options.append(ft.dropdown.Option(key=r.retailer_code, text=r.retailer_name,
                                                                 data=r))
        self._view.dd_retailer.on_change = self.leggi_retailer
        self._view.update_page()
