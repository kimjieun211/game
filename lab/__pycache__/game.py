�
?�Yd  �               @   s�  d  d l  Z  d Z d Z e  j �  e  j j d d g � Z e  j j d � e  j j	 �  Z
 e  j j d � Z d  d  g Z e  j j d � j �  Z e  j j d � j �  Z e j e � d	 Z x� e s�x� e  j j �  D]� Z e j e  j k r� d
 Z n e j e  j k re j �  n  e j e e � e  j j �  Z  e  d  Z! e  d Z" e j e e! e" g � e  j j# �  e
 j$ d � q� We  j% �  q� Wd S)�    N��   i   iX  zCMSC 150 is coolz
laser5.oggz	jieun.jpgzlike.pngFT�   �<   )r   r   r   )r   r   r   )&�pygame�WHITE�BLACK�init�display�set_mode�screen�set_caption�time�Clock�clock�mixer�Sound�click_sound�background_position�image�load�convert�background_image�player_image�set_colorkey�done�event�get�type�QUIT�DONE�MOUSEBUTTONDOWN�play�blit�mouse�get_pos�player_position�x�y�flip�tick�quit� r+   r+   �$C:\Users\admin\Desktop\lab\pygame.py�<module>   s4   
		

