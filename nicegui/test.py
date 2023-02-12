"""
Messing with Python UIs

install
https://github.com/zauberzeug/nicegui/#usage

docs
https://nicegui.io/reference

"""
from nicegui import ui

ui.label('Hello NiceGUI!')
ui.button('BUTTON', on_click=lambda: ui.notify('button was pressed'))

date_result = ui.label()
ui.date(value='2023-01-01', on_change=lambda e: date_result.set_text(e.value))

time_result = ui.label()
ui.time(value='12:00', on_change=lambda e: time_result.set_text(e.value))

ui.run()