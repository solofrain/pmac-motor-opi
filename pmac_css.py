#===========================================================
# This script creates an opi file to display information of
# all PMAC motors.
#
# Usage:
#    Put all motor information list files and this script
#    in the same folder, and run command:
#        python css.py
#
# Input:
#    . $(ioc_server_name)-mtr-info.list
#      Created by pmac_motor.py
#
# Output:
#    . $(beamline)-pmac-motor-info-cntlr.opi
#      This opi file must be in the same folder as
#      pmac-motor-status-1x.opi.
#
#-----------------------------------------------------------
#
# Author:
#    Ji Li <liji@bnl.gov>
#
#===========================================================
import os

#===========================================================
# Start creating an opi file.
# Write independent content.
#===========================================================
def create_opi_start(f, bl):
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    f.write('<display typeId="org.csstudio.opibuilder.Display" version="1.0.0">\n')
    f.write('  <actions hook="false" hook_all="false" />\n')
    f.write('  <auto_scale_widgets>\n')
    f.write('    <auto_scale_widgets>false</auto_scale_widgets>\n')
    f.write('    <min_width>-1</min_width>\n')
    f.write('    <min_height>-1</min_height>\n')
    f.write('  </auto_scale_widgets>\n')
    f.write('  <auto_zoom_to_fit_all>false</auto_zoom_to_fit_all>\n')
    f.write('  <background_color>\n')
    f.write('    <color red="240" green="240" blue="240" />\n')
    f.write('  </background_color>\n')
    f.write('  <boy_version>5.1.0.201706291447</boy_version>\n')
    f.write('  <foreground_color>\n')
    f.write('    <color red="192" green="192" blue="192" />\n')
    f.write('  </foreground_color>\n')
    f.write('  <grid_space>6</grid_space>\n')
    f.write('  <macros>\n')
    f.write('    <include_parent_macros>true</include_parent_macros>\n')
    f.write('    <Mtr>Mtr</Mtr>\n')
    f.write('    <BL>' + bl + '</BL>\n')
    f.write('    <TITLE>$(BL) PMAC MOTOR INFORMATION</TITLE>\n')
    f.write('  </macros>\n')
    f.write('  <name>$(BL) PMAC Motors</name>\n')
    f.write('  <rules />\n')
    f.write('  <scripts />\n')
    f.write('  <show_close_button>true</show_close_button>\n')
    f.write('  <show_edit_range>true</show_edit_range>\n')
    f.write('  <show_grid>true</show_grid>\n')
    f.write('  <show_ruler>true</show_ruler>\n')
    f.write('  <snap_to_geometry>true</snap_to_geometry>\n')
    f.write('  <widget_type>Display</widget_type>\n')
    f.write('  <width>1260</width>\n')
    f.write('  <wuid>1c36ccd2:1676611d681:-5cc2</wuid>\n')
    f.write('  <x>0</x>\n')
    f.write('  <y>0</y>\n')
    f.write('  <widget typeId="org.csstudio.opibuilder.widgets.Image" version="1.0.0">\n')
    f.write('    <actions hook="false" hook_all="false" />\n')
    f.write('    <align_to_nearest_second>false</align_to_nearest_second>\n')
    f.write('    <auto_size>true</auto_size>\n')
    f.write('    <background_color>\n')
    f.write('      <color red="240" green="240" blue="240" />\n')
    f.write('    </background_color>\n')
    f.write('    <border_color>\n')
    f.write('      <color red="0" green="128" blue="255" />\n')
    f.write('    </border_color>\n')
    f.write('    <border_style>0</border_style>\n')
    f.write('    <border_width>1</border_width>\n')
    f.write('    <crop_bottom>0</crop_bottom>\n')
    f.write('    <crop_left>0</crop_left>\n')
    f.write('    <crop_right>0</crop_right>\n')
    f.write('    <crop_top>0</crop_top>\n')
    f.write('    <degree>0</degree>\n')
    f.write('    <enabled>true</enabled>\n')
    f.write('    <flip_horizontal>false</flip_horizontal>\n')
    f.write('    <flip_vertical>false</flip_vertical>\n')
    f.write('    <font>\n')
    f.write('      <opifont.name fontName="Sans" height="10" style="0" pixels="false">Default</opifont.name>\n')
    f.write('    </font>\n')
    f.write('    <foreground_color>\n')
    f.write('      <color red="192" green="192" blue="192" />\n')
    f.write('    </foreground_color>\n')
    f.write('    <height>100</height>\n')
    f.write('    <image_file>/cs-studio-xf/common/Images/NSLS2blue.png</image_file>\n')
    f.write('    <name>Image_2</name>\n')
    f.write('    <no_animation>false</no_animation>\n')
    f.write('    <permutation_matrix>\n')
    f.write('      <row>\n')
    f.write('        <col>1.0</col>\n')
    f.write('        <col>0.0</col>\n')
    f.write('      </row>\n')
    f.write('      <row>\n')
    f.write('        <col>0.0</col>\n')
    f.write('        <col>1.0</col>\n')
    f.write('      </row>\n')
    f.write('    </permutation_matrix>\n')
    f.write('    <rules />\n')
    f.write('    <scale_options>\n')
    f.write('      <width_scalable>true</width_scalable>\n')
    f.write('      <height_scalable>true</height_scalable>\n')
    f.write('      <keep_wh_ratio>false</keep_wh_ratio>\n')
    f.write('    </scale_options>\n')
    f.write('    <scripts />\n')
    f.write('    <stretch_to_fit>false</stretch_to_fit>\n')
    f.write('    <tooltip></tooltip>\n')
    f.write('    <transparency>false</transparency>\n')
    f.write('    <visible>true</visible>\n')
    f.write('    <widget_type>Image</widget_type>\n')
    f.write('    <width>615</width>\n')
    f.write('    <wuid>1c36ccd2:1676611d681:-5618</wuid>\n')
    f.write('    <x>645</x>\n')
    f.write('    <y>0</y>\n')
    f.write('  </widget>\n')
    f.write('  <widget typeId="org.csstudio.opibuilder.widgets.Image" version="1.0.0">\n')
    f.write('    <actions hook="false" hook_all="false" />\n')
    f.write('    <align_to_nearest_second>false</align_to_nearest_second>\n')
    f.write('    <auto_size>true</auto_size>\n')
    f.write('    <background_color>\n')
    f.write('      <color red="240" green="240" blue="240" />\n')
    f.write('    </background_color>\n')
    f.write('    <border_color>\n')
    f.write('      <color red="0" green="128" blue="255" />\n')
    f.write('    </border_color>\n')
    f.write('    <border_style>0</border_style>\n')
    f.write('    <border_width>1</border_width>\n')
    f.write('    <crop_bottom>0</crop_bottom>\n')
    f.write('    <crop_left>0</crop_left>\n')
    f.write('    <crop_right>0</crop_right>\n')
    f.write('    <crop_top>0</crop_top>\n')
    f.write('    <degree>0</degree>\n')
    f.write('    <enabled>true</enabled>\n')
    f.write('    <flip_horizontal>false</flip_horizontal>\n')
    f.write('    <flip_vertical>false</flip_vertical>\n')
    f.write('    <font>\n')
    f.write('      <opifont.name fontName="Sans" height="10" style="0" pixels="false">Default</opifont.name>\n')
    f.write('    </font>\n')
    f.write('    <foreground_color>\n')
    f.write('      <color red="192" green="192" blue="192" />\n')
    f.write('    </foreground_color>\n')
    f.write('    <height>100</height>\n')
    f.write('    <image_file>/cs-studio-xf/common/Images/NSLS2logo.png</image_file>\n')
    f.write('    <name>Image</name>\n')
    f.write('    <no_animation>false</no_animation>\n')
    f.write('    <permutation_matrix>\n')
    f.write('      <row>\n')
    f.write('        <col>1.0</col>\n')
    f.write('        <col>0.0</col>\n')
    f.write('      </row>\n')
    f.write('      <row>\n')
    f.write('        <col>0.0</col>\n')
    f.write('        <col>1.0</col>\n')
    f.write('      </row>\n')
    f.write('    </permutation_matrix>\n')
    f.write('    <rules />\n')
    f.write('    <scale_options>\n')
    f.write('      <width_scalable>true</width_scalable>\n')
    f.write('      <height_scalable>true</height_scalable>\n')
    f.write('      <keep_wh_ratio>false</keep_wh_ratio>\n')
    f.write('    </scale_options>\n')
    f.write('    <scripts />\n')
    f.write('    <stretch_to_fit>false</stretch_to_fit>\n')
    f.write('    <tooltip></tooltip>\n')
    f.write('    <transparency>false</transparency>\n')
    f.write('    <visible>true</visible>\n')
    f.write('    <widget_type>Image</widget_type>\n')
    f.write('    <width>487</width>\n')
    f.write('    <wuid>1c36ccd2:1676611d681:-581e</wuid>\n')
    f.write('    <x>0</x>\n')
    f.write('    <y>0</y>\n')
    f.write('  </widget>\n')
    f.write('  <widget typeId="org.csstudio.opibuilder.widgets.Image" version="1.0.0">\n')
    f.write('    <actions hook="false" hook_all="false" />\n')
    f.write('    <align_to_nearest_second>false</align_to_nearest_second>\n')
    f.write('    <auto_size>true</auto_size>\n')
    f.write('    <background_color>\n')
    f.write('      <color red="240" green="240" blue="240" />\n')
    f.write('    </background_color>\n')
    f.write('    <border_color>\n')
    f.write('      <color red="0" green="128" blue="255" />\n')
    f.write('    </border_color>\n')
    f.write('    <border_style>0</border_style>\n')
    f.write('    <border_width>1</border_width>\n')
    f.write('    <crop_bottom>0</crop_bottom>\n')
    f.write('    <crop_left>0</crop_left>\n')
    f.write('    <crop_right>0</crop_right>\n')
    f.write('    <crop_top>0</crop_top>\n')
    f.write('    <degree>0</degree>\n')
    f.write('    <enabled>true</enabled>\n')
    f.write('    <flip_horizontal>false</flip_horizontal>\n')
    f.write('    <flip_vertical>false</flip_vertical>\n')
    f.write('    <font>\n')
    f.write('      <opifont.name fontName="Sans" height="10" style="0" pixels="false">Default</opifont.name>\n')
    f.write('    </font>\n')
    f.write('    <foreground_color>\n')
    f.write('      <color red="192" green="192" blue="192" />\n')
    f.write('    </foreground_color>\n')
    f.write('    <height>100</height>\n')
    f.write('    <image_file>/cs-studio-xf/common/Images/NSLS2blue.png</image_file>\n')
    f.write('    <name>Image_1</name>\n')
    f.write('    <no_animation>false</no_animation>\n')
    f.write('    <permutation_matrix>\n')
    f.write('      <row>\n')
    f.write('        <col>1.0</col>\n')
    f.write('        <col>0.0</col>\n')
    f.write('      </row>\n')
    f.write('      <row>\n')
    f.write('        <col>0.0</col>\n')
    f.write('        <col>1.0</col>\n')
    f.write('      </row>\n')
    f.write('    </permutation_matrix>\n')
    f.write('    <rules />\n')
    f.write('    <scale_options>\n')
    f.write('      <width_scalable>true</width_scalable>\n')
    f.write('      <height_scalable>true</height_scalable>\n')
    f.write('      <keep_wh_ratio>false</keep_wh_ratio>\n')
    f.write('    </scale_options>\n')
    f.write('    <scripts />\n')
    f.write('    <stretch_to_fit>false</stretch_to_fit>\n')
    f.write('    <tooltip></tooltip>\n')
    f.write('    <transparency>false</transparency>\n')
    f.write('    <visible>true</visible>\n')
    f.write('    <widget_type>Image</widget_type>\n')
    f.write('    <width>615</width>\n')
    f.write('    <wuid>1c36ccd2:1676611d681:-5814</wuid>\n')
    f.write('    <x>486</x>\n')
    f.write('    <y>0</y>\n')
    f.write('  </widget>\n')
    f.write('  <widget typeId="org.csstudio.opibuilder.widgets.Label" version="1.0.0">\n')
    f.write('    <actions hook="false" hook_all="false" />\n')
    f.write('    <auto_size>false</auto_size>\n')
    f.write('    <background_color>\n')
    f.write('      <color red="255" green="255" blue="255" />\n')
    f.write('    </background_color>\n')
    f.write('    <border_color>\n')
    f.write('      <color red="0" green="128" blue="255" />\n')
    f.write('    </border_color>\n')
    f.write('    <border_style>0</border_style>\n')
    f.write('    <border_width>1</border_width>\n')
    f.write('    <enabled>true</enabled>\n')
    f.write('    <font>\n')
    f.write('      <fontdata fontName="Sans" height="22" style="1" pixels="false" />\n')
    f.write('    </font>\n')
    f.write('    <foreground_color>\n')
    f.write('      <color red="0" green="0" blue="0" />\n')
    f.write('    </foreground_color>\n')
    f.write('    <height>100</height>\n')
    f.write('    <horizontal_alignment>1</horizontal_alignment>\n')
    f.write('    <name>Label</name>\n')
    f.write('    <rules />\n')
    f.write('    <scale_options>\n')
    f.write('      <width_scalable>true</width_scalable>\n')
    f.write('      <height_scalable>true</height_scalable>\n')
    f.write('      <keep_wh_ratio>false</keep_wh_ratio>\n')
    f.write('    </scale_options>\n')
    f.write('    <scripts />\n')
    f.write('    <text>$(BL) PMAC MOTOR INFORMATION</text>\n')
    f.write('    <tooltip></tooltip>\n')
    f.write('    <transparent>true</transparent>\n')
    f.write('    <vertical_alignment>1</vertical_alignment>\n')
    f.write('    <visible>true</visible>\n')
    f.write('    <widget_type>Label</widget_type>\n')
    f.write('    <width>774</width>\n')
    f.write('    <wrap_words>false</wrap_words>\n')
    f.write('    <wuid>1c36ccd2:1676611d681:-580e</wuid>\n')
    f.write('    <x>480</x>\n')
    f.write('    <y>0</y>\n')
    f.write('  </widget>\n')
    f.write('\n')

    
#===========================================================
# Write the end of the opi file.
#===========================================================
def create_opi_end(f,height):
    f.write('  <height>' + str(height) + '</height>\n')
    f.write('</display>\n')
    
#===========================================================
# Start creating a container for all motors in the corrent
# collection (same component/PMAC).
#===========================================================
def create_container_begin( f, y, height ):
    
    f.write('  <widget typeId="org.csstudio.opibuilder.widgets.groupingContainer" version="1.0.0">\n')
    f.write('    <actions hook="false" hook_all="false" />\n')
    f.write('    <background_color>\n')
    f.write('      <color red="240" green="240" blue="240" />\n')
    f.write('    </background_color>\n')
    f.write('    <border_color>\n')
    f.write('      <color name="Perm_6" red="33" green="89" blue="103" />\n')
    f.write('    </border_color>\n')
    f.write('    <border_style>1</border_style>\n')
    f.write('    <border_width>1</border_width>\n')
    f.write('    <enabled>true</enabled>\n')
    f.write('    <fc>false</fc>\n')
    f.write('    <font>\n')
    f.write('      <opifont.name fontName="Sans" height="10" style="0" pixels="false">Default</opifont.name>\n')
    f.write('    </font>\n')
    f.write('    <foreground_color>\n')
    f.write('      <color red="192" green="192" blue="192" />\n')
    f.write('    </foreground_color>\n')
    f.write('    <lock_children>false</lock_children>\n')
    f.write('    <name>Grouping Container</name>\n')
    f.write('    <rules />\n')
    f.write('    <scale_options>\n')
    f.write('      <width_scalable>true</width_scalable>\n')
    f.write('      <height_scalable>true</height_scalable>\n')
    f.write('      <keep_wh_ratio>false</keep_wh_ratio>\n')
    f.write('    </scale_options>\n')
    f.write('    <scripts />\n')
    f.write('    <show_scrollbar>true</show_scrollbar>\n')
    f.write('    <tooltip></tooltip>\n')
    f.write('    <transparent>true</transparent>\n')
    f.write('    <visible>true</visible>\n')
    f.write('    <widget_type>Grouping Container</widget_type>\n')
    f.write('    <width>1235</width>\n')
    f.write('    <wuid>1c36ccd2:1676611d681:-5712</wuid>\n')
    f.write('    <x>12</x>\n')
    f.write('    <y>' + str(y) + '</y>\n')


#==========================================================
# Write the end of the container.
#===========================================================
def create_container_end(f, height):
    f.write('    <height>' + str(height) + '</height>\n')
    f.write('  </widget>\n')


#===========================================================
# Create the label background of the container.
#===========================================================
def create_container_label_bg(f, y, height):
    f.write('    <widget typeId="org.csstudio.opibuilder.widgets.Rectangle" version="1.0.0">\n')
    f.write('      <actions hook="false" hook_all="false" />\n')
    f.write('      <alarm_pulsing>false</alarm_pulsing>\n')
    f.write('      <alpha>255</alpha>\n')
    f.write('      <anti_alias>true</anti_alias>\n')
    f.write('      <backcolor_alarm_sensitive>false</backcolor_alarm_sensitive>\n')
    f.write('      <background_color>\n')
    f.write('        <color name="Perm_6" red="33" green="89" blue="103" />\n')
    f.write('      </background_color>\n')
    f.write('      <bg_gradient_color>\n')
    f.write('        <color red="255" green="255" blue="255" />\n')
    f.write('      </bg_gradient_color>\n')
    f.write('      <border_alarm_sensitive>false</border_alarm_sensitive>\n')
    f.write('      <border_color>\n')
    f.write('        <color red="0" green="128" blue="255" />\n')
    f.write('      </border_color>\n')
    f.write('      <border_style>0</border_style>\n')
    f.write('      <border_width>1</border_width>\n')
    f.write('      <enabled>true</enabled>\n')
    f.write('      <fg_gradient_color>\n')
    f.write('        <color red="255" green="255" blue="255" />\n')
    f.write('      </fg_gradient_color>\n')
    f.write('      <fill_level>0.0</fill_level>\n')
    f.write('      <font>\n')
    f.write('        <opifont.name fontName="Sans" height="10" style="0" pixels="false">Default</opifont.name>\n')
    f.write('      </font>\n')
    f.write('      <forecolor_alarm_sensitive>false</forecolor_alarm_sensitive>\n')
    f.write('      <foreground_color>\n')
    f.write('        <color red="255" green="0" blue="0" />\n')
    f.write('      </foreground_color>\n')
    f.write('      <gradient>false</gradient>\n')
    f.write('      <height>' + str(height) + '</height>\n')
    f.write('      <horizontal_fill>true</horizontal_fill>\n')
    f.write('      <line_color>\n')
    f.write('        <color red="128" green="0" blue="255" />\n')
    f.write('      </line_color>\n')
    f.write('      <line_style>0</line_style>\n')
    f.write('      <line_width>0</line_width>\n')
    f.write('      <name>Rectangle</name>\n')
    f.write('      <pv_name></pv_name>\n')
    f.write('      <pv_value />\n')
    f.write('      <rules />\n')
    f.write('      <scale_options>\n')
    f.write('        <width_scalable>true</width_scalable>\n')
    f.write('        <height_scalable>true</height_scalable>\n')
    f.write('        <keep_wh_ratio>false</keep_wh_ratio>\n')
    f.write('      </scale_options>\n')
    f.write('      <scripts />\n')
    f.write('      <tooltip></tooltip>\n')
    f.write('      <transparent>false</transparent>\n')
    f.write('      <visible>true</visible>\n')
    f.write('      <widget_type>Rectangle</widget_type>\n')
    f.write('      <width>137</width>\n')
    f.write('      <wuid>1d074efe:16784cc4d9a:-7e89</wuid>\n')
    f.write('      <x>0</x>\n')
    f.write('      <y>0</y>\n')
    f.write('    </widget>\n')


#===========================================================
# Create the label for the container.
#===========================================================
def create_container_label(f, label, y):
    f.write('    <widget typeId="org.csstudio.opibuilder.widgets.Label" version="1.0.0">\n')
    f.write('      <actions hook="false" hook_all="false" />\n')
    f.write('      <auto_size>false</auto_size>\n')
    f.write('      <background_color>\n')
    f.write('        <color name="Perm_6" red="33" green="89" blue="103" />\n')
    f.write('      </background_color>\n')
    f.write('      <border_color>\n')
    f.write('        <color red="0" green="128" blue="255" />\n')
    f.write('      </border_color>\n')
    f.write('      <border_style>0</border_style>\n')
    f.write('      <border_width>1</border_width>\n')
    f.write('      <enabled>true</enabled>\n')
    f.write('      <font>\n')
    f.write('        <opifont.name fontName="Sans" height="14" style="1" pixels="false">Header 2</opifont.name>\n')
    f.write('      </font>\n')
    f.write('      <foreground_color>\n')
    f.write('        <color name="Group" red="173" green="216" blue="230" />\n')
    f.write('      </foreground_color>\n')
    f.write('      <height>25</height>\n')
    f.write('      <horizontal_alignment>1</horizontal_alignment>\n')
    f.write('      <name>Label_2</name>\n')
    f.write('      <rules />\n')
    f.write('      <scale_options>\n')
    f.write('        <width_scalable>true</width_scalable>\n')
    f.write('        <height_scalable>true</height_scalable>\n')
    f.write('        <keep_wh_ratio>false</keep_wh_ratio>\n')
    f.write('      </scale_options>\n')
    f.write('      <scripts />\n')
    f.write('      <text>' + label + '</text>\n')
    f.write('      <tooltip></tooltip>\n')
    f.write('      <transparent>true</transparent>\n')
    f.write('      <vertical_alignment>1</vertical_alignment>\n')
    f.write('      <visible>true</visible>\n')
    f.write('      <widget_type>Label</widget_type>\n')
    f.write('      <width>137</width>\n')
    f.write('      <wrap_words>false</wrap_words>\n')
    f.write('      <wuid>1c36ccd2:1676611d681:-5644</wuid>\n')
    f.write('      <x>0</x>\n')
    f.write('      <y>' + str(y) + '</y>\n')
    f.write('    </widget>\n')
    
#==========================================================
# Create a widget for the information of one motor.
#===========================================================
def create_motor_status_bar( f, sys, comp, axis, ioc,
                             ioc_srv, cntl_sys, cntl_dev, cntlr_axis,
                             ioc_name, y):

    f.write('    <widget typeId="org.csstudio.opibuilder.widgets.linkingContainer" version="1.0.0">\n')
    f.write('      <actions hook="false" hook_all="false" />\n')
    f.write('      <background_color>\n')
    f.write('        <color red="240" green="240" blue="240" />\n')
    f.write('      </background_color>\n')
    f.write('      <border_color>\n')
    f.write('        <color name="ButtonFG" red="180" green="180" blue="180" />\n')
    f.write('      </border_color>\n')
    f.write('      <border_style>1</border_style>\n')
    f.write('      <border_width>1</border_width>\n')
    f.write('      <enabled>true</enabled>\n')
    f.write('      <font>\n')
    f.write('        <opifont.name fontName="Sans" height="10" style="0" pixels="false">Default</opifont.name>\n')
    f.write('      </font>\n')
    f.write('      <foreground_color>\n')
    f.write('        <color red="192" green="192" blue="192" />\n')
    f.write('      </foreground_color>\n')
    f.write('      <group_name></group_name>\n')
    f.write('      <height>25</height>\n')
    f.write('      <macros>\n')
    f.write('        <include_parent_macros>true</include_parent_macros>\n')
    f.write('        <Sys>' + sys + '</Sys>\n')
    f.write('        <Comp>' + comp + '</Comp>\n')
    f.write('        <Dev>{' + comp + '-Ax:' + axis + '}</Dev>\n')
    f.write('        <Axis>' + axis + '</Axis>\n')
    f.write('        <Ioc>' + ioc + '</Ioc>\n')
    f.write('        <IocSrv>' + ioc_srv + '</IocSrv>\n')
    f.write('        <CntlSys>' + cntl_sys + '</CntlSys>\n')
    f.write('        <CntlDev>' + cntl_dev + '</CntlDev>\n')
    f.write('        <CntlAxis>' + cntl_axis + '</CntlAxis>\n')
    f.write('        <IocName>' + ioc_name + '</IocName>\n')
    f.write('      </macros>\n')
    f.write('      <name>Linking Container_1</name>\n')
    f.write('      <opi_file>pmac-motor-status-1x.opi</opi_file>\n')
    f.write('      <resize_behaviour>1</resize_behaviour>\n')
    f.write('      <rules />\n')
    f.write('      <scale_options>\n')
    f.write('        <width_scalable>true</width_scalable>\n')
    f.write('        <height_scalable>true</height_scalable>\n')
    f.write('        <keep_wh_ratio>true</keep_wh_ratio>\n')
    f.write('      </scale_options>\n')
    f.write('      <scripts />\n')
    f.write('      <tooltip></tooltip>\n')
    f.write('      <visible>true</visible>\n')
    f.write('      <widget_type>Linking Container</widget_type>\n')
    f.write('      <width>936</width>\n')
    f.write('      <wuid>1c36ccd2:1676611d681:-4bc1</wuid>\n')
    f.write('      <x>150</x>\n')
    f.write('      <y>' + str(y) + '</y>\n')
    f.write('    </widget>\n')
    
#==========================================================
# main function
#===========================================================

# merge all list files.
os.system('rm mtr-info.list')
os.system('cat *-mtr-info.list >> mtr-info.list')
list = 'mtr-info.list'

# read information of all motors
info = []
fr = open(list, 'r\n')
for line in fr:
    line = line[:-2]
    line = line.replace(' ','')
    record = line.split('\t')
    info.append(record)
fr.close()

num_axis = len(info)
if num_axis==0:
    print('No motors found. Check for errors!\n')
    exit
    
# create opi per controller
bl = info[0][0][2:6]
opi = bl+'-pmac-motor-info-cntlr.opi'
bl = bl[2:4]
look_index = 1
fw = open(opi, 'w\n')
create_opi_start(fw, info[0][0][2:4] + bl.upper())

i = 0
next_y = 120
# calculate the number of axis in each controller/device
while i< num_axis-1:
    
    new_item_found = 0
    first_axis = info[i][look_index]
    num_axis_cntlr = 1
    for j in range (i+1, num_axis-1):
        if first_axis==info[j][look_index]:
            num_axis_cntlr = num_axis_cntlr + 1
        else:
            first_axis = info[j][look_index]
            new_item_found = 1
            break
    
    # create container
    height = (6+25)*num_axis_cntlr + 8
    create_container_begin(fw, next_y, height)
    tmp = info[i][3]
    create_container_label_bg(fw, next_y, height-2)
    create_container_label(fw, tmp[3:tmp.index('-')], height/2-30)
    create_container_label(fw, info[i][4], height/2+5)
    
    # create bar for each motor
    #       0         1                 2                       3           4       5         6              7        8
    # xf28idc-ioc1    mc01    IOC=XF:28IDC-CT{IOC:MC01}    XF:28IDC-CT    MC:01     1    XF:28IDC-OP:1    Mono:HRM    P    
    y = 0

    for m in range (num_axis_cntlr):
        k = i + m
        sys = info[k][6]
        comp = info[k][7]
        axis  = info[k][8]
        ioc_srv  = info[k][0]
        ioc  = info[k][1]
        ioc_name  = info[k][2]
        cntl_sys = info[k][3]
        cntl_dev  = info[k][4]
        cntl_axis = info[k][5]
        y = y + 6
        create_motor_status_bar( fw, sys, comp, axis, ioc,
                                 ioc_srv, cntl_sys, cntl_dev, cntl_axis,
                                 ioc_name, y);
        y = y + 25
    create_container_end(fw, height)
    
    if (new_item_found==0):
        print('No more controllers.')
        break
    next_y = next_y + height + 10

    # move to next controller/device
    i = j
    
create_opi_end(fw, next_y)

fw.close()
