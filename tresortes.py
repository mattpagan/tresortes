#!/usr/env python
#### bibliomancy.py ####

import wx
import os, glob, sys
import apocrypha
import bible
import webbrowser
import random
from wx.lib.wordwrap import wordwrap


stattext = [
        "Display a random passage from the Bible including the Apocrypha",
        "Display a random passage from the Aeneid",
        "Display a random passage from the Iliad or the Odyssey",
        ]

buttnames = [
    "Sortes \nSanctorum",
    "Sortes \nVirgilianae",
    "Sortes \nHomericae",
    ]

biblebooks = [
    'genesis',
    'exodus',
    'leviticus',
    'numbers',
    'deuteronomy',
    'joshua',
    'judges',
    'ruth',
    '1_samuel',
    '2_samuel',
    '1_kings',
    '2_kings',
    '2_chronicles',
    '1_chronicles',
    'ezra',
    'nehemiah',
    'esther',
    'job',
    'psalms',
    'proverbs',
    'ecclesiastes',
    'songs',
    'isaiah',
    'jeremiah',
    'lamentations',
    'ezekiel',
    'daniel',
    'hosea',
    'joel',
    'amos',
    'obadiah',
    'jonah',
    'micah',
    'nahum',
    'habakkuk',
    'zephaniah',
    'haggai',
    'zechariah',
    'malachi',
    'matthew',
    'mark',
    'luke',
    'john',
    'acts',
    'romans',
    '1_corinthians',
    '2_corinthians',
    'galatians',
    'ephesians',
    'philippians',
    'colossians',
    '1_thessalonians',
    '2_thessalonians',
    '2_timothy',
    '1_timothy',
    'titus',
    'philemon',
    'hebrews',
    'james',
    '1_peter',
    '2_peter',
    '1_john',
    '2_john',
    '3_john',
    'jude',
    'revelation',
]

apocryphabooks = [
    'wisdom_of_solomon',
    'tobit',
    'judith',
    '1_esdras',
    '1_maccabees',
    '2_esdras',
    '2_maccabees',
    'baruch',
    'bel_and_the_dragon',
    'ecclesiasticus',
    'susanna',
    'prayer_of_manasseh',
    'prayer_of_azariah'
    ]

verses = [None, None, None]

verses[0] = ['http://bible.cc/' + book + '/' + verse for book in biblebooks for verse in eval('bible.'+'_'+book)]
verses[0] += ['http://apocrypha.org/' + book + '/' + verse for book in apocryphabooks for verse in eval('apocrypha.'+'_'+book)]

aeneid = range(13) 
aeneid[1]=[1,8,12,34,50,65,76,81,102,124,132,142,157,180,198,208,223,254,272,297,305,325,335,372,387,402,418,441,464,494,520,544,561,579,613,643,657,695,723]
aeneid[2]=[1,13,21,40,57,77,105,145,195,234,250,268,298,318,347,370,402,438,453,469,506,526,559,567,588,624,634,650,671,679,692,752,795]
aeneid[3]=[1,13,19,49,69,84,90,121,135,147,192,258,278,294,320,356,374,441,463,472,506,521,548,570,588,613,655,675,692,716]
aeneid[4]=[1,31,54,90,105,129,160,173,198,219,238,279,296,331,362,393,416,437,450,474,504,522,553,571,584,630,659,693]
aeneid[5]=[1,35,42,72,104,114,124,151,183,225,244,286,315,348,362,387,421,461,485,519,545,575,604,623,664,680,700,719,746,762,779,799,827,852]
aeneid[6]=[1,14,42,77,98,124,156,183,212,236,264,268,282,295,337,384,417,426,477,494,535,548,576,628,637,679,703,724,752,756,801,854,893]
aeneid[7]=[1,5,25,37,45,81,107,135,148,170,192,212,249,286,323,341,373,406,435,445,475,511,540,572,601, 641, 647, 655,670,678,691,706,723,733,744,761,783,803]
aeneid[8]=[1,18,36,66,81,102,126,152,175,184,219,262,280,306,337,370,407,424,454,470,520,541,554,585,608,630,671,729]
aeneid[9]=[1,25,47,77,107,224,246,314,367,420,446,450,459,473,503,525,530,590,621,638,672,691,717,756,778]
aeneid[10]=[1,16,62,96,118,146,163,166,185,198,215,260,276,287,308,345,362,380,399,426,439,479,510,543,575,606,633,653,689,719,747,755,769,791,833,873]
aeneid[11]=[1,29,59,100,122,139,182,203,225,243,296,302,336,445,468,498,522,532,557,597,618,648,664,690,725,768,794,836,868,896]
aeneid[12]=[1,18,54,81,107,113,134,161,175,195,216,238,257,287,311,346,383,411,441,468,500,529,554,593,650,672,697,728,746,766,791,843,869,887,919]

numbook = random.randint(1,12)
verses[1]=['http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.02.0052%3Abook%3D'+str(numbook)+'%3Acard%3D'+str(line) for line in aeneid[numbook] for numbook in xrange(1,13) ] 


iliad = range(25)
iliad[1]=[1,40,80,120,160,200,240,280,320,360,400,440,480,520,560,600]
iliad[2]=[1,40,80,120,160,200,240,280,320,360,400,440,480,520,560,600,640,680,720,760,800,840]
iliad[3]=[1,76,161,243,324,418]
iliad[4]=[1,104,193,265,349,446]
iliad[5]=[1,106,175,274,352,443,572,663,792]
iliad[6]=[1,102,212,305,390,512]
iliad[7]=[1,73,181,287,396,464]
iliad[8]=[1,94,167,253,344,432,542]
iliad[9]=[1,89,182,334,513,644]
iliad[10]=[1,115,177,272,349,431,526]
iliad[11]=[1,99,210,310,384,472,575,668,823]
iliad[12]=[1,172,290,413]
iliad[13]=[1,76,206,266,361,487,581,701,821]
iliad[14]=[1,133,211,296,378,475]
iliad[15]=[1,113,200,281,377,472,592,703]
iliad[16]=[1,131,249,335,431,548,658,751,]
iliad[17]=[1,140,240,342,428,543,626,735,]
iliad[18]=[1,97,183,254,388,497,590,]
iliad[19]=[1,125,249,349,]
iliad[20]=[1,86,199,340,438,]
iliad[21]=[1,114,249,361,424,502,596,]
iliad[22]=[1,141,232,344,416,]
iliad[23]=[1,93,177,287,429,500,596,703,793,884,]
iliad[24]=[1,104,217,314,378,468,571,689,782]
    
odyssey = range(25)
odyssey[1]=[1,44,80,125,178,230,280,325,365,421]
odyssey[2]=[1,39,84,129,177,224,267,309,361,388,]
odyssey[3]=[1,51,102,141,184,229,276,329,371,404,447,]
odyssey[4]=[1,49,100,147,183,219,265,315,351,398,435,481,512,554,593,625,675,715,758,795,]
odyssey[5]=[1,50,92,145,192,228,262,313,365,408,451,]
odyssey[6]=[1,48,85,127,162,211,251,288,]
odyssey[7]=[1,37,77,107,152,198,240,287,317,]
odyssey[8]=[1,46,83,121,165,199,250,295,343,385,433,469,521,550,]
odyssey[9]=[1,47,82,116,161,193,231,281,318,360,409,461,500,536,]
odyssey[10]=[1,46,87,133,178,208,261,302,345,388,428,475,503,546,]
odyssey[11]=[1,51,97,138,180,225,271,321,361,404,440,486,538,567,601,]
odyssey[12]=[1,36,73,111,153,192,234,277,327,364,397,426,]
odyssey[13]=[1,47,93,139,184,217,250,287,329,366,416,]
odyssey[14]=[1,48,72,109,147,191,234,285,321,360,401,446,494,]
odyssey[15]=[1,48,92,130,179,222,265,301,340,380,415,454,493,525,]
odyssey[16]=[1,46,90,135,186,225,266,308,351,393,434,]
odyssey[17]=[1,45,84,120,166,204,247,290,336,380,424,462,505,560,]
odyssey[18]=[1,50,88,124,169,206,250,290,337,365,394,]
odyssey[19]=[1,47,89,148,190,241,277,317,361,405,455,499,544,576,]
odyssey[20]=[1,44,91,133,183,226,268,299,345,]
odyssey[21]=[1,42,80,118,163,205,256,311,354,401,]
odyssey[22]=[1,42,79,126,170,210,255,292,330,378,430,465,]
odyssey[23]=[1,49,85,129,181,231,263,310,344,]
odyssey[24]=[1,35,85,138,191,232,280,327,365,412,450,496]
    

verses[2] = ['http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0136%3Abook%3D'+str(scroll)+'%3Acard%3D'+str(line) for scroll in xrange(1,25) for line in iliad[scroll] ]
verses[2] += ['http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0136%3Abook%3D'+str(scroll)+'%3Acard%3D'+str(line) for scroll in xrange(1,25) for line in odyssey[scroll] ]



class MainWindow(wx.Frame):
    def __init__(self, parent, ID, title):
        wx.Frame.__init__(self, parent, ID, title, size=(350,320))
        self.SetSizeHints(315,285,700,550)
        self.status = self.CreateStatusBar()
        panel = wx.Panel(self, -1)


        textpanel = wx.Panel(panel, -1)
        wordsizer = wx.BoxSizer(wx.HORIZONTAL)
        explanation = wx.StaticText(textpanel, -1, "Bibliomancy is divination by means of literature. A certain \nbook is taken and opened to a page at random. Then the \nquestioner selects a random passage from that page with his \nor her eyes closed. The questioner interprets the passage \nin some way that would relate to the situation at hand. \n \nThe practice was first recorded in ancient Greece using \nHomer's Iliad and Odyssey. The Romans practiced the \ntechnique as well, using their own native epic, Virgil's \nAeneid. Medieval Europe inherited the practice, but adapted \nit for use with the Vulgate of St. Jerome. Although \nbibliomancy can be performed with almost any book, this \nprogram is inspired by the historical origins of the practice.", style=wx.ALIGN_CENTER)
        wordsizer.Add(explanation, 1, wx.ALL | wx.CENTER, 3)
        textpanel.SetSizer(wordsizer)

        hsizer = wx.BoxSizer(wx.HORIZONTAL)
        bookpanel = wx.Panel(panel, -1)

        self.books = range(len(buttnames))
        for i in xrange(len(buttnames)):
            self.books[i] = wx.Button(
                bookpanel, 1, buttnames[i]
                ) #Creates the buttons with names 'self.books[0 - 3]
            
        for i in xrange(len(self.books)):
            hsizer.Add(self.books[i], 1, wx.ALL, 8)
        bookpanel.SetSizer(hsizer)

        for i in xrange(len(self.books)):
            self.books[i].Bind(wx.EVT_ENTER_WINDOW, self.OnBook )
            self.books[i].Bind(wx.EVT_LEAVE_WINDOW, self.OnClear )
            self.Bind(wx.EVT_BUTTON, self.OnSortes, self.books[i])
            


        ## Sizer for the whole panel
        s = wx.BoxSizer(wx.VERTICAL)
        s.Add(textpanel, 6, wx.EXPAND | wx.ALL, 3)
        s.Add(bookpanel, 2, wx.EXPAND | wx.ALL, 3)
        panel.SetSizer(s)

        self.Bind(wx.EVT_CONTEXT_MENU, self.OnContextMenu)

    def OnSortes(self, event):
        global verses
        thisbook = self.books.index(event.GetEventObject())
        webbrowser.open(random.choice(verses[thisbook]))
        
    def OnClear(self, event):
        self.SetStatusText("")
        event.Skip()

    def OnBook(self, event):
        self.SetStatusText(stattext[self.books.index(event.GetEventObject())])
        event.Skip()

    def OnContextMenu(self, event):
        self.popupID1 = wx.NewId()
        self.Bind(wx.EVT_MENU, self.OnAbout, id=self.popupID1)
       
        # right click menu
        menu = wx.Menu()
        menu.Append(self.popupID1, "About")
        self.PopupMenu(menu)
        menu.Destroy()

    def OnAbout(self, event):
        info = wx.AboutDialogInfo()
        info.Name = "Tresortes"
        info.Copyright = "(C) 2012 Matt Pagan\n"
        info.Description = wordwrap(            
            "Tresortes is written using wxPython.",
            350, wx.ClientDC(self))
        info.License = wordwrap(
            "This program is free software: you can redistribute it and/or "
            "modify it under the terms of the GNU General Public License as "
            "published by the Free Software Foundation, either version 3 of "
            "the License, or (at your option) any later version. ",
            250, wx.ClientDC(self))
        wx.AboutBox(info)



############################## End MainWindow ########################

if __name__ == '__main__':
    app = wx.App(False)
    frame = MainWindow(None, -1, "Tresortes")
##    frame.SetIcon(wx.Icon('hexico2.ico', wx.BITMAP_TYPE_ICO))
    
    frame.Show()
    app.MainLoop()
