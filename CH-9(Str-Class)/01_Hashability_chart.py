""" Hashability table ====>>>

hash means mapping

just like built-in function eg= print(), input() etc
which lies in the built-in module

similarly hash is also a built-in function 


++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+                                      +                                 +
+                         Hashable     +      Mutable                    +
+   int                   yes          +      no                         +
+   float                 yes          +      no                         +
+   complex               yes          +      no                         +
+   bool                  yes          +      no                         +
+   str                   yes          +      no                         +
+   range                 yes          +      no                         +
+   list                  no           +      yes                        +
+   tuple                 yes          +      no                         +
+   set                   no           +      yes                        +
+   dict                  no           +      yes                        +
+                                      +                                 +
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""

x=5;
print(type(x));

print(hash(x));

y=4.5;
print(type(y),hash(y),sep=" ");

z=4.5;
print(hash(z));
