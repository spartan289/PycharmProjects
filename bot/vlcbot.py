from pywinauto import Application
app = Application(backend='uia')
app.connect(title_re=".*Chrome.*")
dlg = app.top_window()
url = dlg.child_window(title="Adreso ir paieškos juosta", control_type="Edit").get_value()
print(url)