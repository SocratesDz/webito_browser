#!/usr/bin/env python2
#-*- coding: utf-8 -*-

import pygtk
pygtk.require('2.0')
import gtk
import webkit
import sys

class WebitoBrowser:
	def __init__(self):
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.set_position(gtk.WIN_POS_CENTER)
		self.window.set_default_size(800, 600)
		self.window.connect("destroy", self.on_quit)

		vbox = gtk.VBox()	# Creando un VBox (captain obvious was here)

		# Un campo de texto para la url
		self.url_text = gtk.Entry()
		self.url_text.connect("activate", self.url_text_activate)

		# Una scroll para la ventana
		self.scroll_window = gtk.ScrolledWindow()
		self.webview = webkit.WebView()	# webkit
		self.scroll_window.add(self.webview)	# agregamos el webview al ScrolledWindow

		# Agregamos los widgets al VBox
		vbox.pack_start(self.url_text, fill=True, expand=False)
		vbox.pack_start(self.scroll_window, True, True)
		
		# Mostramos todo
		self.window.add(vbox)
		self.window.show_all()

	def url_text_activate(self, entry):
		self.open_url(entry.get_text())

	def on_quit(self, widget):
		gtk.main_quit()

	def open_url(self, url):
		self.window.set_title("%s - Webito" % url)
		self.url_text.set_text(url)
		self.webview.open(url)

if __name__ == '__main__':
	browser = WebitoBrowser()
	browser.open_url(sys.argv[1])
	gtk.main()


