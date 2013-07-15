####################################
# PyEdit: A python text editor     #
# Made by: Emma Jones (AwwCookies) #
####################################
import pygtk, gtk, pango, urllib2, urllib
import gtkcodebuffer, os, json, sys
class PyEdit:
    #CONIG
    def get_config(self):
        self.CONFIG = {
            "font": "Ubuntu Mono 12",
        }
        
    def __init__(self, File = None):
        self.get_config()
        self.VERSION = "0.0.2"
        self.PROGNAME = "PyEdit"
        # syntax hilighting
        self.lang = None
        self.buff = None
        self.FILEPATH = ""
        # self.FILEEXT = ""
        self.syntax = None
        self.FONT = pango.FontDescription(self.CONFIG["font"])
        self.SEP = gtk.SeparatorMenuItem()
        self.clipboard = gtk.Clipboard()
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_title("PyEdit")
        self.window.set_size_request(800, 600)
        # self.window.set_icon_from_file(gtk.STOCK_FILE)
        self.window.connect("delete_event", self.delete_event)
        self.window.connect("destroy", self.destory)
        self.window.connect("key_press_event", self.key_pressed)

        self.menubar = gtk.MenuBar()
        self.filemenu = gtk.Menu()
        self.file_menu = gtk.MenuItem("File")

        self.helpmenu = gtk.Menu()
        self.help_menu = gtk.MenuItem("Help")

        self.settingsmenu = gtk.Menu()
        self.settings_menu = gtk.MenuItem("Settings")

        self.editmenu = gtk.Menu()
        self.edit_menu = gtk.MenuItem("Edit")

        self.uploadmenu = gtk.Menu()
        self.upload_menu = gtk.MenuItem("Upload")

        self.syntaxmenu = gtk.Menu()
        self.syntax_menu = gtk.MenuItem("Syntax")
        
        self.help_menu_about = gtk.MenuItem("About")
        self.help_menu_about.connect("activate", self.about_dialog)

        self.file_menu_open = gtk.MenuItem("Open")
        self.file_menu_open.connect("activate", self.open)

        self.file_menu_save_as = gtk.MenuItem("Save As")
        self.file_menu_save_as.connect("activate", self.save_as)

        self.file_menu_save = gtk.MenuItem("Save")
        self.file_menu_save.connect("activate", self.save)

        self.file_menu_exit = gtk.MenuItem("Exit")
        self.file_menu_exit.connect("activate", gtk.main_quit)
        
        self.file_menu_new = gtk.MenuItem("New")
        self.file_menu_new.connect("activate", self.new)

        self.settings_menu_font = gtk.MenuItem("Font")
        self.settings_menu_font.connect("activate", self.font_dialog)

        self.edit_menu_cut = gtk.MenuItem("Cut")
        self.edit_menu_cut.connect("activate", self.cut)
        self.edit_menu_copy = gtk.MenuItem("Copy")
        self.edit_menu_copy.connect("activate", self.copy)
        self.edit_menu_paste = gtk.MenuItem("Paste")
        self.edit_menu_paste.connect("activate", self.paste)

        # self.upload_menu_cookiebin = gtk.MenuItem("CookieBin")
        # self.upload_menu_cookiebin.connect("activate", self.cookiebin)
        
        # self.upload_menu_pastebin = gtk.MenuItem("Pastebin")
        # self.upload_menu_pastebin.connect("activate", self.pastebin)
        
        # Create all the syntax menu items
        self.syntax_menu_ada = gtk.MenuItem("ada")
        self.syntax_menu_c = gtk.MenuItem("c")
        self.syntax_menu_changelog = gtk.MenuItem("changelog")
        self.syntax_menu_cpp = gtk.MenuItem("cpp")
        self.syntax_menu_csharp = gtk.MenuItem("csharp")
        self.syntax_menu_css = gtk.MenuItem("css")
        self.syntax_menu_desktop = gtk.MenuItem("desktop")
        self.syntax_menu_diff = gtk.MenuItem("diff")
        self.syntax_menu_fortran = gtk.MenuItem("fortran")
        self.syntax_menu_gtkrc = gtk.MenuItem("gtkrc")
        # self.syntax_menu_haskell = gtk.MenuItem("haskell")
        self.syntax_menu_html = gtk.MenuItem("html")
        self.syntax_menu_idl = gtk.MenuItem("idl")
        self.syntax_menu_ini = gtk.MenuItem("ini")
        self.syntax_menu_java = gtk.MenuItem("java")
        self.syntax_menu_javascript = gtk.MenuItem("javascript")
        self.syntax_menu_latex = gtk.MenuItem("latex")
        self.syntax_menu_lua = gtk.MenuItem("lua")
        self.syntax_menu_makefile = gtk.MenuItem("makefile")
        self.syntax_menu_markdown = gtk.MenuItem("markdown")
        self.syntax_menu_msil = gtk.MenuItem("msil")
        self.syntax_menu_nemerle = gtk.MenuItem("nemerle")
        self.syntax_menu_none = gtk.MenuItem("none")
        self.syntax_menu_octave = gtk.MenuItem("octave")
        self.syntax_menu_pascal = gtk.MenuItem("pascal")
        self.syntax_menu_perl = gtk.MenuItem("perl")
        self.syntax_menu_php = gtk.MenuItem("php")
        self.syntax_menu_po = gtk.MenuItem("po")
        self.syntax_menu_python = gtk.MenuItem("python")
        self.syntax_menu_R = gtk.MenuItem("R")
        self.syntax_menu_ruby = gtk.MenuItem("ruby")
        self.syntax_menu_scheme = gtk.MenuItem("scheme")
        self.syntax_menu_sh = gtk.MenuItem("sh")
        self.syntax_menu_sql = gtk.MenuItem("sql")
        self.syntax_menu_tcl = gtk.MenuItem("tcl")
        self.syntax_menu_texinfo = gtk.MenuItem("texinfo")
        self.syntax_menu_vbnet = gtk.MenuItem("vbnet")
        self.syntax_menu_verilog = gtk.MenuItem("verilog")
        self.syntax_menu_vhdl = gtk.MenuItem("vhdl")
        self.syntax_menu_xml = gtk.MenuItem("xml")

        # Connect all the syntax menu items to the change_syntax function
        self.syntax_menu_ada.connect("activate", self.change_syntax)
        self.syntax_menu_c.connect("activate", self.change_syntax)
        self.syntax_menu_changelog.connect("activate", self.change_syntax)
        self.syntax_menu_cpp.connect("activate", self.change_syntax)
        self.syntax_menu_csharp.connect("activate", self.change_syntax)
        self.syntax_menu_css.connect("activate", self.change_syntax)
        self.syntax_menu_desktop.connect("activate", self.change_syntax)
        self.syntax_menu_diff.connect("activate", self.change_syntax)
        self.syntax_menu_fortran.connect("activate", self.change_syntax)
        self.syntax_menu_gtkrc.connect("activate", self.change_syntax)
        # self.syntax_menu_haskell.connect("activate", self.change_syntax)
        self.syntax_menu_html.connect("activate", self.change_syntax)
        self.syntax_menu_idl.connect("activate", self.change_syntax)
        self.syntax_menu_ini.connect("activate", self.change_syntax)
        self.syntax_menu_java.connect("activate", self.change_syntax)
        self.syntax_menu_javascript.connect("activate", self.change_syntax)
        self.syntax_menu_latex.connect("activate", self.change_syntax)
        self.syntax_menu_lua.connect("activate", self.change_syntax)
        self.syntax_menu_makefile.connect("activate", self.change_syntax)
        self.syntax_menu_markdown.connect("activate", self.change_syntax)
        self.syntax_menu_msil.connect("activate", self.change_syntax)
        self.syntax_menu_nemerle.connect("activate", self.change_syntax)
        self.syntax_menu_none.connect("activate", self.change_syntax)
        self.syntax_menu_octave.connect("activate", self.change_syntax)
        self.syntax_menu_pascal.connect("activate", self.change_syntax)
        self.syntax_menu_perl.connect("activate", self.change_syntax)
        self.syntax_menu_php.connect("activate", self.change_syntax)
        self.syntax_menu_po.connect("activate", self.change_syntax)
        self.syntax_menu_python.connect("activate", self.change_syntax)
        self.syntax_menu_R.connect("activate", self.change_syntax)
        self.syntax_menu_ruby.connect("activate", self.change_syntax)
        self.syntax_menu_scheme.connect("activate", self.change_syntax)
        self.syntax_menu_sh.connect("activate", self.change_syntax)
        self.syntax_menu_sql.connect("activate", self.change_syntax)
        self.syntax_menu_tcl.connect("activate", self.change_syntax)
        self.syntax_menu_texinfo.connect("activate", self.change_syntax)
        self.syntax_menu_vbnet.connect("activate", self.change_syntax)
        self.syntax_menu_verilog.connect("activate", self.change_syntax)
        self.syntax_menu_vhdl.connect("activate", self.change_syntax)
        self.syntax_menu_xml.connect("activate", self.change_syntax)

        # Appended all the syntax_menus to the main syntaxmenu
        self.syntaxmenu.append(self.syntax_menu_ada)
        self.syntaxmenu.append(self.syntax_menu_c)
        self.syntaxmenu.append(self.syntax_menu_changelog)
        self.syntaxmenu.append(self.syntax_menu_cpp)
        self.syntaxmenu.append(self.syntax_menu_csharp)
        self.syntaxmenu.append(self.syntax_menu_css)
        self.syntaxmenu.append(self.syntax_menu_desktop)
        self.syntaxmenu.append(self.syntax_menu_diff)
        self.syntaxmenu.append(self.syntax_menu_fortran)
        self.syntaxmenu.append(self.syntax_menu_gtkrc)
        # self.syntaxmenu.append(self.syntax_menu_haskell)
        self.syntaxmenu.append(self.syntax_menu_html)
        self.syntaxmenu.append(self.syntax_menu_idl)
        self.syntaxmenu.append(self.syntax_menu_ini)
        self.syntaxmenu.append(self.syntax_menu_java)
        self.syntaxmenu.append(self.syntax_menu_javascript)
        self.syntaxmenu.append(self.syntax_menu_latex)
        self.syntaxmenu.append(self.syntax_menu_lua)
        self.syntaxmenu.append(self.syntax_menu_makefile)
        self.syntaxmenu.append(self.syntax_menu_markdown)
        self.syntaxmenu.append(self.syntax_menu_msil)
        self.syntaxmenu.append(self.syntax_menu_nemerle)
        self.syntaxmenu.append(self.syntax_menu_none)
        self.syntaxmenu.append(self.syntax_menu_octave)
        self.syntaxmenu.append(self.syntax_menu_pascal)
        self.syntaxmenu.append(self.syntax_menu_perl)
        self.syntaxmenu.append(self.syntax_menu_php)
        self.syntaxmenu.append(self.syntax_menu_po)
        self.syntaxmenu.append(self.syntax_menu_python)
        self.syntaxmenu.append(self.syntax_menu_R)
        self.syntaxmenu.append(self.syntax_menu_ruby)
        self.syntaxmenu.append(self.syntax_menu_scheme)
        self.syntaxmenu.append(self.syntax_menu_sh)
        self.syntaxmenu.append(self.syntax_menu_sql)
        self.syntaxmenu.append(self.syntax_menu_tcl)
        self.syntaxmenu.append(self.syntax_menu_texinfo)
        self.syntaxmenu.append(self.syntax_menu_vbnet)
        self.syntaxmenu.append(self.syntax_menu_verilog)
        self.syntaxmenu.append(self.syntax_menu_vhdl)
        self.syntaxmenu.append(self.syntax_menu_xml)

        self.filemenu.append(self.file_menu_new)
        self.filemenu.append(self.file_menu_open)
        self.filemenu.append(self.file_menu_save)
        self.filemenu.append(self.file_menu_save_as)
        self.filemenu.append(self.SEP)
        self.filemenu.append(self.file_menu_exit)

        self.settingsmenu.append(self.settings_menu_font)

        self.editmenu.append(self.edit_menu_cut)
        self.editmenu.append(self.edit_menu_copy)
        self.editmenu.append(self.edit_menu_paste)

        # self.uploadmenu.append(self.upload_menu_cookiebin)
        # self.uploadmenu.append(self.upload_menu_pastebin)

        self.helpmenu.append(self.help_menu_about)

        self.file_menu.set_submenu(self.filemenu)
        self.edit_menu.set_submenu(self.editmenu)
        self.upload_menu.set_submenu(self.uploadmenu)
        self.settings_menu.set_submenu(self.settingsmenu)
        self.syntax_menu.set_submenu(self.syntaxmenu)
        self.help_menu.set_submenu(self.helpmenu)
           
        self.menubar.append(self.file_menu)
        self.menubar.append(self.edit_menu)
        self.menubar.append(self.settings_menu)
        # self.menubar.append(self.upload_menu)
        self.menubar.append(self.syntax_menu)
        self.menubar.append(self.help_menu)
        
        self.vbox = gtk.VBox(False, 2)   
        
        self.textview = gtk.TextView()
        self.textview.set_buffer(self.buff)
        self.textview.modify_font(self.FONT)
        if File != None:
            self.textview.get_buffer().set_text(open(File, 'rb').read())
        self.textview.set_wrap_mode(True)
        self.scrollwindow = gtk.ScrolledWindow()
        self.scrollwindow.add_with_viewport(self.textview)
        
        self.label = gtk.Label()
        
        self.vbox.pack_start(self.menubar, False, False, 0)
        self.vbox.pack_start(self.scrollwindow)
        self.vbox.pack_start(self.label, False, False, 0)

        self.window.add(self.vbox)
        self.window.show_all()
    
    def new(self, widget, data = None):   
        self.textview.get_buffer().set_text("")
        self.label.set_text("")
    
    def about_dialog(self, widget, data = None):
        self.ad = gtk.AboutDialog()
        self.ad.set_name(self.PROGNAME)
        self.ad.set_version(self.VERSION)
        self.ad.set_authors(["Emma Jones (AwwCookies)"])
        self.ad.set_website("http://github.com/AwwCookies/PyEdit")
        self.ad.set_comments(
            "Text Editor made with python and GTK\n\n"
            "Syntax highlighting made possible with Code Buffer\n"
            "http://code.google.com/p/pygtkcodebuffer/")
        self.ad.set_default_response(gtk.RESPONSE_OK)
        self.response = self.ad.run()
        self.ad.destroy()
        
    def change_syntax(self, widget, data = None):
        # Save current buffer text
        self.old_buffer = self.textview.get_buffer().get_text(self.textview.get_buffer().get_start_iter(),
            self.textview.get_buffer().get_end_iter())
        if widget != None:
            if widget.get_label() != "none":
                self.syntax = gtkcodebuffer.SyntaxLoader(widget.get_label())
                self.buff = gtkcodebuffer.CodeBuffer(lang=self.syntax, font=self.FONT)
            else:
                self.buff = None
            self.textview.set_buffer(self.buff)
            # Restore Buffer text
            self.textview.get_buffer().set_text(self.old_buffer)
        else:
            self.buff = gtkcodebuffer.CodeBuffer(lang=self.syntax, font=self.FONT)
            self.textview.set_buffer(self.buff)
            self.textview.get_buffer().set_text(self.old_buffer)
        # self.label.set_text("Path: %s Syntax: %s" % (self.FILEPATH, widget.get_label()))
            
        
    def font_dialog(self, widget, data = None):
        self.dialog = gtk.FontSelectionDialog("Pick a font")
        self.dialog.set_font_name(self.FONT.to_string())
        self.dialog.run()
        self.FONT = pango.FontDescription(self.dialog.get_font_name())
        self.textview.modify_font(self.FONT)
        self.change_syntax(None)
        self.dialog.destroy()
    
    def open(self, widget, data = None):
        self.dialog = gtk.FileChooserDialog(
            "Open...", None, gtk.FILE_CHOOSER_ACTION_OPEN, (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
            gtk.STOCK_OPEN, gtk.RESPONSE_OK))

        self.dialog.set_default_response(gtk.RESPONSE_OK)
        self.filter = gtk.FileFilter()
        self.filter.set_name("All files")
        self.filter.add_pattern("*.*")

        self.dialog.add_filter(self.filter)
        self.response = self.dialog.run()
        if self.response == gtk.RESPONSE_OK:
            self.text = []
            self.window.set_title("PyEdit: " + self.dialog.get_filename().split("/")[-1])
            self.label.set_text(self.dialog.get_filename())
            self.FILEPATH = self.dialog.get_filename()
            with open(self.dialog.get_filename(), "rb") as f:
                for self.line in f:
                    self.text.append(self.line)
            self.textview.get_buffer().set_text(''.join(self.text))
        self.dialog.destroy()
    
    def save_as(self, widget, data = None):
        self.dialog = gtk.FileChooserDialog(
            "Save...", None, gtk.FILE_CHOOSER_ACTION_SAVE, (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
            gtk.STOCK_SAVE, gtk.RESPONSE_OK))
        self.dialog.set_default_response(gtk.RESPONSE_OK)
        
        self.response = self.dialog.run()
        if self.response == gtk.RESPONSE_OK:
            self.FILEPATH = self.dialog.get_filename()
            # self.FILEEXT = self.dialog.get_filename().split("/")[-1].split(".")[1]
            self.label.set_text(self.FILEPATH)
            with open(self.FILEPATH, "wb") as f:
                f.write(self.textview.get_buffer().get_text(self.textview.get_buffer().get_start_iter(),
                        self.textview.get_buffer().get_end_iter()))
        self.dialog.destroy()
    
    def save(self, widget, data = None):
        if self.FILEPATH != "":
            with open(self.FILEPATH, "wb") as f:
                f.write(self.textview.get_buffer().get_text(self.textview.get_buffer().get_start_iter(),
                        self.textview.get_buffer().get_end_iter()))
        else:
            self.save_as(widget, data)
    
    def delete_event(self, widget, event, data = None):
        return False
    
    def destory(self, widget, data = None):
        gtk.main_quit()
    
    def cut(self, widget, data = None):
        self.textview.get_buffer().cut_clipboard(self.clipboard, self.textview.get_editable())

    def copy(self, widget, data = None):
        self.textview.get_buffer().copy_clipboard(self.clipboard)

    def paste(self, widget, data = None):
        self.textview.get_buffer().paste_clipboard(self.clipboard, None, self.textview.get_editable())
    
    def key_pressed(self, widget, data = None):
        pass
    
    def main(self):
        gtk.main()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        PyEdit = PyEdit(sys.argv[1])
    else:
        PyEdit = PyEdit()
    PyEdit.main()
    
    
    
    
    
    
    
    
    
    
