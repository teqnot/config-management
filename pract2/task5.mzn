enum MenuVer = {M1_0_0, M1_1_0, M1_2_0, M1_3_0, M1_4_0, M1_5_0};
enum DropdownVer = {D1_8_0, D2_0_0, D2_1_0, D2_2_0, D2_3_0};
enum IconsVer = {I1_0_0, I2_0_0};

var MenuVer: menu;
var DropdownVer: dropdown;
var IconsVer: icons;

constraint
  (menu == M1_5_0 -> dropdown in {D2_3_0} /\ icons in {I2_0_0}) /\
  (menu == M1_4_0 -> dropdown in {D2_2_0, D2_3_0} /\ icons in {I2_0_0}) /\
  (menu == M1_3_0 -> dropdown in {D2_1_0, D2_2_0, D2_3_0} /\ icons in {I2_0_0}) /\
  (menu == M1_2_0 -> dropdown in {D2_0_0, D2_1_0, D2_2_0, D2_3_0} /\ icons in {I2_0_0}) /\
  (menu == M1_1_0 -> dropdown in {D1_8_0, D2_0_0, D2_1_0, D2_2_0, D2_3_0} /\ icons in {I1_0_0, I2_0_0}) /\
  (menu == M1_0_0 -> dropdown in {D1_8_0, D2_0_0, D2_1_0, D2_2_0, D2_3_0} /\ icons in {I1_0_0, I2_0_0});

solve satisfy;
