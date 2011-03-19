format 75

classcanvas 128002 class_ref 128002 // Gracz
  class_drawing_mode default show_context_mode default show_stereotype_properties default
  xyz 38 105 2000
end
usecasecanvas 128130 usecase_ref 128130 // Zaloguj
  xyzwh 181 55 3005 64 32 label_xy 192 87
end
usecasecanvas 128258 usecase_ref 128258 // Zaloz gre
  xyzwh 257 216 3005 64 32 label_xy 260 246
end
usecasecanvas 128642 usecase_ref 128386 // Pobierz liste oczekujacych gier
  xyzwh 175 276 3005 64 32 label_xy 123 308
end
usecasecanvas 128898 usecase_ref 129026 // Wyloguj
  xyzwh 280 127 3005 64 32 label_xy 290 159
end
line 128386 ----
  from ref 128002 z 3006 to ref 128130
line 128514 ----
  from ref 128002 z 3006 to ref 128258
line 128770 ----
  from ref 128002 z 3006 to ref 128642
line 129026 ----
  from ref 128002 z 3006 to ref 128898
end
