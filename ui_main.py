# Form implementation generated from reading ui file '.\QtUI\ui_main_window.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 646)
        MainWindow.setMinimumSize(QtCore.QSize(900, 646))
        MainWindow.setMaximumSize(QtCore.QSize(900, 646))
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(9, 9, 881, 581))
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.stackedWidget.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.label_pg1 = QtWidgets.QLabel(self.page_1)
        self.label_pg1.setGeometry(QtCore.QRect(800, 0, 40, 18))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        self.label_pg1.setFont(font)
        self.label_pg1.setObjectName("label_pg1")
        self.gb_Config = QtWidgets.QGroupBox(self.page_1)
        self.gb_Config.setGeometry(QtCore.QRect(0, 20, 880, 280))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.gb_Config.setFont(font)
        self.gb_Config.setFlat(True)
        self.gb_Config.setObjectName("gb_Config")
        self.label01 = QtWidgets.QLabel(self.gb_Config)
        self.label01.setGeometry(QtCore.QRect(20, 30, 130, 24))
        self.label01.setObjectName("label01")
        self.txt_ExePath = QtWidgets.QLineEdit(self.gb_Config)
        self.txt_ExePath.setGeometry(QtCore.QRect(20, 60, 751, 24))
        self.txt_ExePath.setObjectName("txt_ExePath")
        self.btn_ExePath = QtWidgets.QPushButton(self.gb_Config)
        self.btn_ExePath.setGeometry(QtCore.QRect(790, 60, 75, 24))
        self.btn_ExePath.setObjectName("btn_ExePath")
        self.label02 = QtWidgets.QLabel(self.gb_Config)
        self.label02.setGeometry(QtCore.QRect(20, 90, 130, 24))
        self.label02.setObjectName("label02")
        self.btn_IPF = QtWidgets.QPushButton(self.gb_Config)
        self.btn_IPF.setGeometry(QtCore.QRect(790, 120, 75, 24))
        self.btn_IPF.setObjectName("btn_IPF")
        self.txt_IPF = QtWidgets.QLineEdit(self.gb_Config)
        self.txt_IPF.setGeometry(QtCore.QRect(20, 120, 751, 24))
        self.txt_IPF.setObjectName("txt_IPF")
        self.label03 = QtWidgets.QLabel(self.gb_Config)
        self.label03.setGeometry(QtCore.QRect(20, 150, 130, 24))
        self.label03.setObjectName("label03")
        self.btn_OPD = QtWidgets.QPushButton(self.gb_Config)
        self.btn_OPD.setGeometry(QtCore.QRect(790, 180, 75, 24))
        self.btn_OPD.setObjectName("btn_OPD")
        self.txt_OPD = QtWidgets.QLineEdit(self.gb_Config)
        self.txt_OPD.setGeometry(QtCore.QRect(20, 180, 751, 24))
        self.txt_OPD.setObjectName("txt_OPD")
        self.cb_OpenOPD = QtWidgets.QCheckBox(self.gb_Config)
        self.cb_OpenOPD.setGeometry(QtCore.QRect(40, 210, 247, 22))
        self.cb_OpenOPD.setObjectName("cb_OpenOPD")
        self.cb_LoadVis = QtWidgets.QCheckBox(self.gb_Config)
        self.cb_LoadVis.setGeometry(QtCore.QRect(40, 240, 247, 22))
        self.cb_LoadVis.setObjectName("cb_LoadVis")
        self.gb_Process = QtWidgets.QGroupBox(self.page_1)
        self.gb_Process.setGeometry(QtCore.QRect(0, 300, 880, 280))
        self.gb_Process.setFlat(True)
        self.gb_Process.setObjectName("gb_Process")
        self.label04 = QtWidgets.QLabel(self.gb_Process)
        self.label04.setGeometry(QtCore.QRect(20, 30, 32, 24))
        self.label04.setObjectName("label04")
        self.txt_Log = QtWidgets.QTextBrowser(self.gb_Process)
        self.txt_Log.setGeometry(QtCore.QRect(60, 80, 811, 192))
        self.txt_Log.setSource(QtCore.QUrl(""))
        self.txt_Log.setObjectName("txt_Log")
        self.label05 = QtWidgets.QLabel(self.gb_Process)
        self.label05.setGeometry(QtCore.QRect(20, 80, 32, 24))
        self.label05.setObjectName("label05")
        self.lbl_Status = QtWidgets.QLabel(self.gb_Process)
        self.lbl_Status.setGeometry(QtCore.QRect(60, 30, 711, 24))
        self.lbl_Status.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.lbl_Status.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.lbl_Status.setObjectName("lbl_Status")
        self.lbl_Status.setStyleSheet("font-style:italic; text-align:center; color:red")
        self.lbl_Status.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.btn_Exec = QtWidgets.QPushButton(self.gb_Process)
        self.btn_Exec.setGeometry(QtCore.QRect(790, 30, 75, 24))
        self.btn_Exec.setObjectName("btn_Exec")
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_pg2 = QtWidgets.QLabel(self.page_2)
        self.label_pg2.setGeometry(QtCore.QRect(800, 0, 40, 18))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        self.label_pg2.setFont(font)
        self.label_pg2.setObjectName("label_pg2")
        self.gb_Plots = QtWidgets.QGroupBox(self.page_2)
        self.gb_Plots.setGeometry(QtCore.QRect(305, 20, 575, 560))
        self.gb_Plots.setFlat(False)
        self.gb_Plots.setCheckable(False)
        self.gb_Plots.setObjectName("gb_Plots")
        self.lw_PltList = QtWidgets.QListWidget(self.gb_Plots)
        self.lw_PltList.setGeometry(QtCore.QRect(385, 310, 180, 205))
        self.lw_PltList.setObjectName("lw_PltList")
        self.lw_StdList = QtWidgets.QListWidget(self.gb_Plots)
        self.lw_StdList.setGeometry(QtCore.QRect(385, 40, 180, 205))
        self.lw_StdList.setObjectName("lw_StdList")
        self.btn_PltNew = QtWidgets.QPushButton(self.gb_Plots)
        self.btn_PltNew.setGeometry(QtCore.QRect(385, 520, 70, 24))
        self.btn_PltNew.setObjectName("btn_PltNew")
        self.btn_PltDlt = QtWidgets.QPushButton(self.gb_Plots)
        self.btn_PltDlt.setGeometry(QtCore.QRect(495, 520, 70, 24))
        self.btn_PltDlt.setObjectName("btn_PltDlt")
        self.label20 = QtWidgets.QLabel(self.gb_Plots)
        self.label20.setGeometry(QtCore.QRect(385, 290, 80, 20))
        self.label20.setObjectName("label20")
        self.label19 = QtWidgets.QLabel(self.gb_Plots)
        self.label19.setGeometry(QtCore.QRect(385, 20, 80, 20))
        self.label19.setObjectName("label19")
        self.btn_StdLoad = QtWidgets.QPushButton(self.gb_Plots)
        self.btn_StdLoad.setGeometry(QtCore.QRect(385, 250, 70, 24))
        self.btn_StdLoad.setObjectName("btn_StdLoad")
        self.btn_StdRemove = QtWidgets.QPushButton(self.gb_Plots)
        self.btn_StdRemove.setGeometry(QtCore.QRect(495, 250, 70, 24))
        self.btn_StdRemove.setObjectName("btn_StdRemove")
        self.gb_PlotConfigs = QtWidgets.QGroupBox(self.gb_Plots)
        self.gb_PlotConfigs.setGeometry(QtCore.QRect(10, 30, 365, 315))
        self.gb_PlotConfigs.setFlat(True)
        self.gb_PlotConfigs.setObjectName("gb_PlotConfigs")
        self.cb_Trace = QtWidgets.QComboBox(self.gb_PlotConfigs)
        self.cb_Trace.setGeometry(QtCore.QRect(60, 90, 110, 24))
        self.cb_Trace.setObjectName("cb_Trace")
        self.label22 = QtWidgets.QLabel(self.gb_PlotConfigs)
        self.label22.setGeometry(QtCore.QRect(10, 55, 65, 24))
        self.label22.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label22.setObjectName("label22")
        self.cb_Style = QtWidgets.QComboBox(self.gb_PlotConfigs)
        self.cb_Style.setGeometry(QtCore.QRect(60, 120, 110, 24))
        self.cb_Style.setObjectName("cb_Style")
        self.label25 = QtWidgets.QLabel(self.gb_PlotConfigs)
        self.label25.setGeometry(QtCore.QRect(10, 120, 40, 24))
        self.label25.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label25.setObjectName("label25")
        self.label23 = QtWidgets.QLabel(self.gb_PlotConfigs)
        self.label23.setGeometry(QtCore.QRect(10, 90, 40, 24))
        self.label23.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label23.setObjectName("label23")
        self.label24 = QtWidgets.QLabel(self.gb_PlotConfigs)
        self.label24.setGeometry(QtCore.QRect(185, 90, 50, 24))
        self.label24.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label24.setObjectName("label24")
        self.cb_FillArea = QtWidgets.QCheckBox(self.gb_PlotConfigs)
        self.cb_FillArea.setEnabled(True)
        self.cb_FillArea.setGeometry(QtCore.QRect(245, 90, 110, 24))
        self.cb_FillArea.setObjectName("cb_FillArea")
        self.cb_TicksX = QtWidgets.QCheckBox(self.gb_PlotConfigs)
        self.cb_TicksX.setEnabled(True)
        self.cb_TicksX.setGeometry(QtCore.QRect(245, 120, 50, 24))
        self.cb_TicksX.setChecked(True)
        self.cb_TicksX.setObjectName("cb_TicksX")
        self.txt_TicksX = QtWidgets.QLineEdit(self.gb_PlotConfigs)
        self.txt_TicksX.setEnabled(False)
        self.txt_TicksX.setGeometry(QtCore.QRect(305, 120, 50, 24))
        self.txt_TicksX.setText("")
        self.txt_TicksX.setFrame(True)
        self.txt_TicksX.setObjectName("txt_TicksX")
        self.cb_TicksY = QtWidgets.QCheckBox(self.gb_PlotConfigs)
        self.cb_TicksY.setEnabled(True)
        self.cb_TicksY.setGeometry(QtCore.QRect(245, 150, 50, 24))
        self.cb_TicksY.setChecked(True)
        self.cb_TicksY.setObjectName("cb_TicksY")
        self.txt_TicksY = QtWidgets.QLineEdit(self.gb_PlotConfigs)
        self.txt_TicksY.setEnabled(False)
        self.txt_TicksY.setGeometry(QtCore.QRect(305, 150, 50, 24))
        self.txt_TicksY.setText("")
        self.txt_TicksY.setObjectName("txt_TicksY")
        self.label26 = QtWidgets.QLabel(self.gb_PlotConfigs)
        self.label26.setGeometry(QtCore.QRect(185, 120, 50, 24))
        self.label26.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label26.setObjectName("label26")
        self.label27 = QtWidgets.QLabel(self.gb_PlotConfigs)
        self.label27.setGeometry(QtCore.QRect(185, 150, 50, 24))
        self.label27.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label27.setObjectName("label27")
        self.label28 = QtWidgets.QLabel(self.gb_PlotConfigs)
        self.label28.setGeometry(QtCore.QRect(10, 185, 100, 24))
        self.label28.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label28.setObjectName("label28")
        self.label31 = QtWidgets.QLabel(self.gb_PlotConfigs)
        self.label31.setGeometry(QtCore.QRect(115, 215, 40, 24))
        self.label31.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label31.setObjectName("label31")
        self.sb_Row = QtWidgets.QSpinBox(self.gb_PlotConfigs)
        self.sb_Row.setGeometry(QtCore.QRect(160, 185, 50, 24))
        self.sb_Row.setMinimum(1)
        self.sb_Row.setMaximum(12)
        self.sb_Row.setObjectName("sb_Row")
        self.label29 = QtWidgets.QLabel(self.gb_PlotConfigs)
        self.label29.setGeometry(QtCore.QRect(115, 185, 40, 24))
        self.label29.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label29.setObjectName("label29")
        self.sb_Col = QtWidgets.QSpinBox(self.gb_PlotConfigs)
        self.sb_Col.setGeometry(QtCore.QRect(160, 215, 50, 24))
        self.sb_Col.setMinimum(1)
        self.sb_Col.setMaximum(12)
        self.sb_Col.setObjectName("sb_Col")
        self.label30 = QtWidgets.QLabel(self.gb_PlotConfigs)
        self.label30.setGeometry(QtCore.QRect(235, 185, 60, 24))
        self.label30.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label30.setObjectName("label30")
        self.sb_RowSpan = QtWidgets.QSpinBox(self.gb_PlotConfigs)
        self.sb_RowSpan.setGeometry(QtCore.QRect(305, 185, 50, 24))
        self.sb_RowSpan.setMinimum(1)
        self.sb_RowSpan.setMaximum(12)
        self.sb_RowSpan.setEnabled(False)
        self.sb_RowSpan.setObjectName("sb_RowSpan")
        self.sb_ColSpan = QtWidgets.QSpinBox(self.gb_PlotConfigs)
        self.sb_ColSpan.setGeometry(QtCore.QRect(305, 215, 50, 24))
        self.sb_ColSpan.setMinimum(1)
        self.sb_ColSpan.setMaximum(12)
        self.sb_ColSpan.setEnabled(False)
        self.sb_ColSpan.setObjectName("sb_ColSpan")
        self.label32 = QtWidgets.QLabel(self.gb_PlotConfigs)
        self.label32.setGeometry(QtCore.QRect(235, 215, 60, 24))
        self.label32.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label32.setObjectName("label32")
        self.label21 = QtWidgets.QLabel(self.gb_PlotConfigs)
        self.label21.setGeometry(QtCore.QRect(10, 30, 85, 24))
        self.label21.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label21.setObjectName("label21")
        self.label33 = QtWidgets.QLabel(self.gb_PlotConfigs)
        self.label33.setGeometry(QtCore.QRect(10, 250, 100, 24))
        self.label33.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label33.setObjectName("label33")
        self.cb_StatMean = QtWidgets.QCheckBox(self.gb_PlotConfigs)
        self.cb_StatMean.setEnabled(True)
        self.cb_StatMean.setGeometry(QtCore.QRect(120, 250, 110, 24))
        self.cb_StatMean.setObjectName("cb_StatMean")
        self.cb_StatMedian = QtWidgets.QCheckBox(self.gb_PlotConfigs)
        self.cb_StatMedian.setEnabled(True)
        self.cb_StatMedian.setGeometry(QtCore.QRect(120, 280, 110, 24))
        self.cb_StatMedian.setObjectName("cb_StatMedian")
        self.layoutWidget = QtWidgets.QWidget(self.gb_PlotConfigs)
        self.layoutWidget.setGeometry(QtCore.QRect(105, 30, 251, 24))
        self.layoutWidget.setObjectName("layoutWidget")
        self.rb_group1 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.rb_group1.setContentsMargins(0, 0, 0, 0)
        self.rb_group1.setObjectName("rb_group1")
        self.rb_Selective = QtWidgets.QRadioButton(self.layoutWidget)
        self.rb_Selective.setChecked(True)
        self.rb_Selective.setObjectName("rb_Selective")
        self.rb_group1.addWidget(self.rb_Selective)
        self.rb_Collective = QtWidgets.QRadioButton(self.layoutWidget)
        self.rb_Collective.setChecked(False)
        self.rb_Collective.setObjectName("rb_Collective")
        self.rb_group1.addWidget(self.rb_Collective)
        self.layoutWidget1 = QtWidgets.QWidget(self.gb_PlotConfigs)
        self.layoutWidget1.setGeometry(QtCore.QRect(85, 55, 271, 24))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.rb_group2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.rb_group2.setContentsMargins(0, 0, 0, 0)
        self.rb_group2.setObjectName("rb_group2")
        self.rb_HourlyVal = QtWidgets.QRadioButton(self.layoutWidget1)
        self.rb_HourlyVal.setChecked(True)
        self.rb_HourlyVal.setObjectName("rb_HourlyVal")
        self.rb_group2.addWidget(self.rb_HourlyVal)
        self.rb_MonthlyVal = QtWidgets.QRadioButton(self.layoutWidget1)
        self.rb_MonthlyVal.setObjectName("rb_MonthlyVal")
        self.rb_group2.addWidget(self.rb_MonthlyVal)
        self.rb_AnnualVal = QtWidgets.QRadioButton(self.layoutWidget1)
        self.rb_AnnualVal.setObjectName("rb_AnnualVal")
        self.rb_group2.addWidget(self.rb_AnnualVal)
        self.gb_SeriesX = QtWidgets.QGroupBox(self.gb_Plots)
        self.gb_SeriesX.setGeometry(QtCore.QRect(10, 355, 365, 120))
        self.gb_SeriesX.setFlat(True)
        self.gb_SeriesX.setObjectName("gb_SeriesX")
        self.cb_Xdata = QtWidgets.QComboBox(self.gb_SeriesX)
        self.cb_Xdata.setGeometry(QtCore.QRect(110, 90, 245, 24))
        self.cb_Xdata.setObjectName("cb_Xdata")
        self.cb_Xstart = QtWidgets.QComboBox(self.gb_SeriesX)
        self.cb_Xstart.setGeometry(QtCore.QRect(150, 25, 130, 24))
        self.cb_Xstart.setEditable(True)
        self.cb_Xstart.setObjectName("cb_Xstart")
        self.label34 = QtWidgets.QLabel(self.gb_SeriesX)
        self.label34.setGeometry(QtCore.QRect(110, 25, 30, 24))
        self.label34.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label34.setObjectName("label34")
        self.label35 = QtWidgets.QLabel(self.gb_SeriesX)
        self.label35.setGeometry(QtCore.QRect(110, 55, 30, 24))
        self.label35.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label35.setObjectName("label35")
        self.cb_Xend = QtWidgets.QComboBox(self.gb_SeriesX)
        self.cb_Xend.setGeometry(QtCore.QRect(150, 55, 130, 24))
        self.cb_Xend.setEditable(True)
        self.cb_Xend.setObjectName("cb_Xend")
        self.rb_Xtime = QtWidgets.QRadioButton(self.gb_SeriesX)
        self.rb_Xtime.setChecked(True)
        self.rb_Xtime.setGeometry(QtCore.QRect(10, 25, 90, 24))
        self.rb_Xtime.setObjectName("rb_Xtime")
        self.rb_Xdata = QtWidgets.QRadioButton(self.gb_SeriesX)
        self.rb_Xdata.setGeometry(QtCore.QRect(10, 90, 90, 24))
        self.rb_Xdata.setObjectName("rb_Xdata")
        self.gb_SeriesY = QtWidgets.QGroupBox(self.gb_Plots)
        self.gb_SeriesY.setGeometry(QtCore.QRect(10, 485, 365, 50))
        self.gb_SeriesY.setFlat(True)
        self.gb_SeriesY.setObjectName("gb_SeriesY")
        self.cb_Ydata = QtWidgets.QComboBox(self.gb_SeriesY)
        self.cb_Ydata.setGeometry(QtCore.QRect(110, 20, 245, 24))
        self.cb_Ydata.setObjectName("cb_Ydata")
        self.gb_Figures = QtWidgets.QGroupBox(self.page_2)
        self.gb_Figures.setGeometry(QtCore.QRect(0, 20, 295, 440))
        self.gb_Figures.setFlat(False)
        self.gb_Figures.setObjectName("gb_Figures")
        self.lw_FigList = QtWidgets.QListWidget(self.gb_Figures)
        self.lw_FigList.setGeometry(QtCore.QRect(90, 185, 195, 185))
        self.lw_FigList.setObjectName("lw_FigList")
        self.btn_FigDlt = QtWidgets.QPushButton(self.gb_Figures)
        self.btn_FigDlt.setGeometry(QtCore.QRect(215, 155, 70, 24))
        self.btn_FigDlt.setObjectName("btn_FigDlt")
        self.label14 = QtWidgets.QLabel(self.gb_Figures)
        self.label14.setGeometry(QtCore.QRect(10, 185, 70, 24))
        self.label14.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label14.setObjectName("label14")
        self.btn_FigAdd = QtWidgets.QPushButton(self.gb_Figures)
        self.btn_FigAdd.setGeometry(QtCore.QRect(90, 155, 70, 24))
        self.btn_FigAdd.setObjectName("btn_FigAdd")
        self.label06 = QtWidgets.QLabel(self.gb_Figures)
        self.label06.setGeometry(QtCore.QRect(10, 30, 70, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.label06.setFont(font)
        self.label06.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label06.setObjectName("label06")
        self.txt_FigName = QtWidgets.QLineEdit(self.gb_Figures)
        self.txt_FigName.setGeometry(QtCore.QRect(90, 30, 195, 24))
        self.txt_FigName.setObjectName("txt_FigName")
        self.label07 = QtWidgets.QLabel(self.gb_Figures)
        self.label07.setGeometry(QtCore.QRect(10, 60, 70, 24))
        self.label07.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label07.setObjectName("label07")
        self.sb_FigCols = QtWidgets.QSpinBox(self.gb_Figures)
        self.sb_FigCols.setGeometry(QtCore.QRect(235, 60, 50, 24))
        self.sb_FigCols.setMinimum(1)
        self.sb_FigCols.setMaximum(12)
        self.sb_FigCols.setObjectName("sb_FigCols")
        self.label08 = QtWidgets.QLabel(self.gb_Figures)
        self.label08.setGeometry(QtCore.QRect(90, 60, 40, 24))
        self.label08.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label08.setObjectName("label08")
        self.sb_FigRows = QtWidgets.QSpinBox(self.gb_Figures)
        self.sb_FigRows.setGeometry(QtCore.QRect(135, 60, 50, 24))
        self.sb_FigRows.setMinimum(1)
        self.sb_FigRows.setMaximum(12)
        self.sb_FigRows.setObjectName("sb_FigRows")
        self.label09 = QtWidgets.QLabel(self.gb_Figures)
        self.label09.setGeometry(QtCore.QRect(190, 60, 40, 24))
        self.label09.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label09.setObjectName("label09")
        self.label10 = QtWidgets.QLabel(self.gb_Figures)
        self.label10.setGeometry(QtCore.QRect(10, 90, 70, 24))
        self.label10.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label10.setObjectName("label10")
        self.label11 = QtWidgets.QLabel(self.gb_Figures)
        self.label11.setGeometry(QtCore.QRect(90, 90, 40, 24))
        self.label11.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label11.setObjectName("label11")
        self.label12 = QtWidgets.QLabel(self.gb_Figures)
        self.label12.setGeometry(QtCore.QRect(190, 90, 40, 24))
        self.label12.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label12.setObjectName("label12")
        self.txt_FigWidth = QtWidgets.QLineEdit(self.gb_Figures)
        self.txt_FigWidth.setGeometry(QtCore.QRect(135, 90, 50, 24))
        self.txt_FigWidth.setObjectName("txt_FigWidth")
        self.txt_FigHeight = QtWidgets.QLineEdit(self.gb_Figures)
        self.txt_FigHeight.setGeometry(QtCore.QRect(235, 90, 50, 24))
        self.txt_FigHeight.setObjectName("txt_FigHeight")
        self.label15 = QtWidgets.QLabel(self.gb_Figures)
        self.label15.setGeometry(QtCore.QRect(10, 380, 70, 24))
        self.label15.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label15.setObjectName("label15")
        self.cb_FileFormat = QtWidgets.QComboBox(self.gb_Figures)
        self.cb_FileFormat.setGeometry(QtCore.QRect(90, 380, 105, 24))
        self.cb_FileFormat.setCurrentText("")
        self.cb_FileFormat.setObjectName("cb_FileFormat")
        self.btn_FigSave = QtWidgets.QPushButton(self.gb_Figures)
        self.btn_FigSave.setGeometry(QtCore.QRect(205, 410, 80, 24))
        self.btn_FigSave.setObjectName("btn_FigSave")
        self.btn_FigView = QtWidgets.QPushButton(self.gb_Figures)
        self.btn_FigView.setGeometry(QtCore.QRect(90, 410, 105, 24))
        self.btn_FigView.setObjectName("btn_FigView")
        self.btn_FigLoad = QtWidgets.QPushButton(self.gb_Figures)
        self.btn_FigLoad.setEnabled(False)
        self.btn_FigLoad.setGeometry(QtCore.QRect(205, 380, 80, 24))
        self.btn_FigLoad.setObjectName("btn_FigLoad")
        self.label13 = QtWidgets.QLabel(self.gb_Figures)
        self.label13.setGeometry(QtCore.QRect(10, 120, 70, 24))
        self.label13.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label13.setObjectName("label13")
        self.sb_FontSize = QtWidgets.QSpinBox(self.gb_Figures)
        self.sb_FontSize.setGeometry(QtCore.QRect(90, 120, 50, 24))
        self.sb_FontSize.setMinimum(9)
        self.sb_FontSize.setMaximum(35)
        self.sb_FontSize.setProperty("value", 16)
        self.sb_FontSize.setObjectName("sb_FontSize")
        self.cb_Legend = QtWidgets.QCheckBox(self.gb_Figures)
        self.cb_Legend.setEnabled(True)
        self.cb_Legend.setGeometry(QtCore.QRect(165, 120, 100, 24))
        self.cb_Legend.setObjectName("cb_Legend")
        self.gb_Info = QtWidgets.QGroupBox(self.page_2)
        self.gb_Info.setGeometry(QtCore.QRect(0, 460, 295, 120))
        self.gb_Info.setObjectName("gb_Info")
        self.label16 = QtWidgets.QLabel(self.gb_Info)
        self.label16.setGeometry(QtCore.QRect(10, 30, 95, 24))
        self.label16.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label16.setObjectName("label16")
        self.label17 = QtWidgets.QLabel(self.gb_Info)
        self.label17.setGeometry(QtCore.QRect(10, 60, 95, 24))
        self.label17.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label17.setObjectName("label17")
        self.label18 = QtWidgets.QLabel(self.gb_Info)
        self.label18.setGeometry(QtCore.QRect(10, 90, 95, 24))
        self.label18.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label18.setObjectName("label18")
        self.lbl_SlctFig = QtWidgets.QLabel(self.gb_Info)
        self.lbl_SlctFig.setGeometry(QtCore.QRect(115, 30, 170, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.lbl_SlctFig.setFont(font)
        self.lbl_SlctFig.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.lbl_SlctFig.setObjectName("lbl_SlctFig")
        self.lbl_SlctFig.setStyleSheet("border-bottom-width: 1px; border-bottom-style: solid; border-radius: 0px; color: red;")
        self.lbl_SlctPlt = QtWidgets.QLabel(self.gb_Info)
        self.lbl_SlctPlt.setGeometry(QtCore.QRect(115, 60, 170, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.lbl_SlctPlt.setFont(font)
        self.lbl_SlctPlt.setObjectName("lbl_SlctPlt")
        self.lbl_SlctPlt.setStyleSheet("border-bottom-width: 1px; border-bottom-style: solid; border-radius: 0px; color: red;")
        self.lbl_SlctStd = QtWidgets.QLabel(self.gb_Info)
        self.lbl_SlctStd.setGeometry(QtCore.QRect(115, 90, 170, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.lbl_SlctStd.setFont(font)
        self.lbl_SlctStd.setObjectName("lbl_SlctStd")
        self.lbl_SlctStd.setStyleSheet("border-bottom-width: 1px; border-bottom-style: solid; border-radius: 0px; color: red;")
        
        self.gb_Config.setStyleSheet("QGroupBox {font-weight: bold;}")
        self.gb_Figures.setStyleSheet("QGroupBox {font-weight: bold;}")
        self.gb_Info.setStyleSheet("QGroupBox {font-weight: bold;}")
        self.gb_Plots.setStyleSheet("QGroupBox {font-weight: bold;}")
        self.gb_Process.setStyleSheet("QGroupBox {font-weight: bold;}")
        self.stackedWidget.addWidget(self.page_2)
        self.btn_Page = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Page.setGeometry(QtCore.QRect(850, 8, 30, 21))
        self.btn_Page.setObjectName("btn_Page")
        self.btn_Page.setFlat(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 24))
        self.menubar.setObjectName("menubar")
        self.m_Menu = QtWidgets.QMenu(self.menubar)
        self.m_Menu.setObjectName("m_Menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionEnergy_Balance_Compilation = QtGui.QAction(MainWindow)
        self.actionEnergy_Balance_Compilation.setObjectName("actionEnergy_Balance_Compilation")
        self.actionInstalled_Capacities_Compilation = QtGui.QAction(MainWindow)
        self.actionInstalled_Capacities_Compilation.setObjectName("actionInstalled_Capacities_Compilation")
        self.m_Menu.addAction(self.actionAbout)
        self.m_Menu.addAction(self.actionExit)
        self.menubar.addAction(self.m_Menu.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.cb_FileFormat.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EnergyPLAN Visualizer"))
        self.label_pg1.setText(_translate("MainWindow", "Page 1"))
        self.gb_Config.setTitle(_translate("MainWindow", "Configuration"))
        self.label01.setText(_translate("MainWindow", "EnergyPLAN .exe Path:"))
        self.btn_ExePath.setText(_translate("MainWindow", "Select"))
        self.label02.setText(_translate("MainWindow", "Input File Path:"))
        self.btn_IPF.setText(_translate("MainWindow", "Select"))
        self.label03.setText(_translate("MainWindow", "Output Directory:"))
        self.btn_OPD.setText(_translate("MainWindow", "Browse"))
        self.cb_OpenOPD.setText(_translate("MainWindow", "Open output directiry after processing"))
        self.cb_LoadVis.setText(_translate("MainWindow", "Load Study to Visualizer"))
        self.gb_Process.setTitle(_translate("MainWindow", "Process"))
        self.label04.setText(_translate("MainWindow", "State:"))
        self.label05.setText(_translate("MainWindow", "Log:"))
        self.lbl_Status.setText(_translate("MainWindow", "Use the options above to process a study input file"))
        self.btn_Exec.setText(_translate("MainWindow", "Execute"))
        self.label_pg2.setText(_translate("MainWindow", "Page 2"))
        self.gb_Plots.setTitle(_translate("MainWindow", "Plots"))
        self.btn_PltNew.setText(_translate("MainWindow", "New"))
        self.btn_PltDlt.setText(_translate("MainWindow", "Delete"))
        self.label20.setText(_translate("MainWindow", "Plots List:"))
        self.label19.setText(_translate("MainWindow", "Studies List:"))
        self.btn_StdLoad.setText(_translate("MainWindow", "Load"))
        self.btn_StdRemove.setText(_translate("MainWindow", "Remove"))
        self.gb_PlotConfigs.setTitle(_translate("MainWindow", "Plot Configurations:"))
        self.label22.setText(_translate("MainWindow", "Data Type:"))
        self.label25.setText(_translate("MainWindow", "Style:"))
        self.label23.setText(_translate("MainWindow", "Trace:"))
        self.label24.setText(_translate("MainWindow", "Options:"))
        self.cb_FillArea.setText(_translate("MainWindow", "Fill Under Lines"))
        self.cb_TicksX.setText(_translate("MainWindow", "Auto"))
        self.txt_TicksX.setInputMask(_translate("MainWindow", "0009"))
        self.cb_TicksY.setText(_translate("MainWindow", "Auto"))
        self.txt_TicksY.setInputMask(_translate("MainWindow", "0009"))
        self.label26.setText(_translate("MainWindow", "X Ticks"))
        self.label27.setText(_translate("MainWindow", "Y Ticks"))
        self.label28.setText(_translate("MainWindow", "Position in Grid:"))
        self.label31.setText(_translate("MainWindow", "Col"))
        self.label29.setText(_translate("MainWindow", "Row"))
        self.label30.setText(_translate("MainWindow", "Row Span"))
        self.label32.setText(_translate("MainWindow", "Col Span"))
        self.label21.setText(_translate("MainWindow", "Analysis Type:"))
        self.label33.setText(_translate("MainWindow", "Statistical Lines:"))
        self.cb_StatMean.setText(_translate("MainWindow", "Draw Mean"))
        self.cb_StatMedian.setText(_translate("MainWindow", "Draw Median"))
        self.rb_Selective.setText(_translate("MainWindow", "Selective"))
        self.rb_Collective.setText(_translate("MainWindow", "Collective"))
        self.rb_HourlyVal.setText(_translate("MainWindow", "Hourly"))
        self.rb_MonthlyVal.setText(_translate("MainWindow", "Monthly"))
        self.rb_AnnualVal.setText(_translate("MainWindow", "Annual"))
        self.gb_SeriesX.setTitle(_translate("MainWindow", "Range (X Axis):"))
        self.label34.setText(_translate("MainWindow", "From"))
        self.label35.setText(_translate("MainWindow", "To"))
        self.rb_Xtime.setText(_translate("MainWindow", "Time Series"))
        self.rb_Xdata.setText(_translate("MainWindow", "Data Series"))
        self.gb_SeriesY.setTitle(_translate("MainWindow", "Data (Y Axis):"))
        self.gb_Figures.setTitle(_translate("MainWindow", "Figures"))
        self.btn_FigDlt.setText(_translate("MainWindow", "Delete"))
        self.label14.setText(_translate("MainWindow", "Figuers List:"))
        self.btn_FigAdd.setText(_translate("MainWindow", "Add"))
        self.label06.setText(_translate("MainWindow", "Name:"))
        self.label07.setText(_translate("MainWindow", "Grid:"))
        self.label08.setText(_translate("MainWindow", "Rows"))
        self.label09.setText(_translate("MainWindow", "Cols"))
        self.label10.setText(_translate("MainWindow", "Size (Pixels):"))
        self.label11.setText(_translate("MainWindow", "Width"))
        self.label12.setText(_translate("MainWindow", "Height"))
        self.txt_FigWidth.setInputMask(_translate("MainWindow", "0009"))
        self.txt_FigWidth.setText(_translate("MainWindow", "1366"))
        self.txt_FigHeight.setInputMask(_translate("MainWindow", "0009"))
        self.txt_FigHeight.setText(_translate("MainWindow", "768"))
        self.label15.setText(_translate("MainWindow", "File Format:"))
        self.btn_FigSave.setText(_translate("MainWindow", "Save"))
        self.btn_FigView.setText(_translate("MainWindow", "Preview"))
        self.btn_FigLoad.setText(_translate("MainWindow", "Load"))
        self.label13.setText(_translate("MainWindow", "Font Size:"))
        self.cb_Legend.setText(_translate("MainWindow", "Show Legend"))
        self.gb_Info.setTitle(_translate("MainWindow", "Information"))
        self.label16.setText(_translate("MainWindow", "Selected Figure:"))
        self.label17.setText(_translate("MainWindow", "Selected Plot:"))
        self.label18.setText(_translate("MainWindow", "Selected Study:"))
        self.lbl_SlctFig.setText(_translate("MainWindow", "none"))
        self.lbl_SlctPlt.setText(_translate("MainWindow", "none"))
        self.lbl_SlctStd.setText(_translate("MainWindow", "none"))
        self.btn_Page.setText(_translate("MainWindow", "\u2B9C\u2B9E"))
        self.m_Menu.setTitle(_translate("MainWindow", "Menu"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionEnergy_Balance_Compilation.setText(_translate("MainWindow", "Energy Balance Compilation"))
        self.actionInstalled_Capacities_Compilation.setText(_translate("MainWindow", "Installed Capacities Compilation"))
