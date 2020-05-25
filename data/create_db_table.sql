drop database if exists gamedata;
create database gamedata;

use gamedata;

DROP TABLE IF EXISTS fortnite;
CREATE TABLE fortnite(
date DATETIME
,time TIME
,rank INT(4)
,mental VARCHAR(100)
,eliminations INT(2)
,assist INT(2)
,revive INT(2)
,accuracy VARCHAR(100)
,hit INT(3)
,hs INT(3)
,distance FLOAT(8)
,material INT(5)
,material_used INT(5)
,damage INT(4)
,damage_to_players INT(4)
,damage_to_structures INT(5)
)
;

DROP TABLE IF EXISTS pkmn;
CREATE TABLE pokemon(
# INT(100)
,Name VARCHAR(100)
,Type VARCHAR(100)
,Total INT(4)
,HP INT(4)
,Attack INT(4)
,Defense INT(4)
,SpAtk INT(4)
,SpDef INT(4)
,Speed INT(4)
)
;

DROP TABLE IF EXISTS rocket_deadzone_settings;
CREATE TABLE rocket_deadzone_settings(
Player VARCHAR(100)
,Team VARCHAR(100)
,Deadzone_Shape VARCHAR(100)
,Deadzone FLOAT(5)
,Dodge_Deadzone FLOAT(5)
,Aerial_Sensivity FLOAT(5)
,Steering_Sensivity FLOAT(5)
,Last_Update DATETIME
)
;

DROP TABLE IF EXISTS rocket_cam_settings;
CREATE TABLE rocket_cam_settings(
Player VARCHAR(100)
,Team VARCHAR(100)
,Camera_Shake VARCHAR(100)
,FOV VARCHAR(3)
,Height VARCHAR(3)
,Angle VARCHAR(5)
,Distance INT(3)
,Stiffness VARCHAR(5)
,Swivel_Speed FLOAT(5)
,Transition_Speed FLOAT(5)
,Ball_Camera VARCHAR(100)
,Last_Update DATETIME
,A_Distance FLOAT(10)
,A_FOV FLOAT(10)
,A_Height FLOAT(10)
,A_Angle FLOAT(10)
,A_Stiffness FLOAT(10)
)
;

DROP TABLE IF EXISTS rocket_cam_settings_desc_6;
CREATE TABLE rocket_cam_settings_desc_6(
    FOV_DESC INT(5)
    ,Distance_DESC INT(5)
    ,Height_DESC INT(5)
    ,Angle_DESC INT(5)
)
;