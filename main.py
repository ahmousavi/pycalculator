import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

builder = Gtk.Builder.new_from_file("ui.glade")
class PyCalculator():
      def __init__(self):
            self.win = builder.get_object("main_window")
            self.txtIO = builder.get_object("txtIO")
            self.win.show_all()
      def on_main_window_remove(self, window, event):
            Gtk.main_quit()

      def on_btnNumber_clicked(self, btn):
            txt = self.txtIO.get_text()
            if txt == 'error':
                  self.txtIO.set_text('')
                  txt = ''
            if len(txt) < 18:
                  self.txtIO.set_text(txt + btn.get_label())
      def on_btnSymbol_clicked(self, btn):
            txt = self.txtIO.get_text()
            if len(txt) == 0:
                  return
            
            if len(txt) < 16:
                  self.txtIO.set_text(txt + btn.get_label())
      def on_btnEq_clicked(self, btn):
            phrase = self.txtIO.get_text()
            try:
                  result = eval(phrase)
            except:
                  self.txtIO.set_text('error')
                  return
            if int(result) == result:
                  self.txtIO.set_text(str(int(result)))
            else:      
                  self.txtIO.set_text(str(result))
      
      def on_btnBack_clicked(self, btn):
            txt = self.txtIO.get_text()
            if txt == 'error':
                  self.txtIO.set_text('')
            elif len(txt) > 0:
                  self.txtIO.set_text(txt[:-1])

builder.connect_signals(PyCalculator())
     
PyCalculator()
Gtk.main()
