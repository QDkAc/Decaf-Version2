VTABLE(_Main) {
    <empty>
    Main
}

VTABLE(_Sorted) {
    <empty>
    Sorted
    _Sorted.init;
    _Sorted.print;
    _Sorted.merge;
}

FUNCTION(_Main_New) {
memo ''
_Main_New:
    _T8 = 4
    parm _T8
    _T9 =  call _Alloc
    _T10 = VTBL <_Main>
    *(_T9 + 0) = _T10
    return _T9
}

FUNCTION(_Sorted_New) {
memo ''
_Sorted_New:
    _T11 = 12
    parm _T11
    _T12 =  call _Alloc
    _T13 = 0
    *(_T12 + 4) = _T13
    *(_T12 + 8) = _T13
    _T14 = VTBL <_Sorted>
    *(_T12 + 0) = _T14
    return _T12
}

FUNCTION(_Main.sort) {
memo '_T0:4 _T1:8 _T2:12'
_Main.sort:
    _T15 = 1
    _T16 = (_T1 + _T15)
    _T17 = (_T16 >= _T2)
    if (_T17 == 0) branch _L15
    _T19 =  call _Sorted_New
    _T18 = _T19
    _T20 = *(_T0 + 0)
    _T21 = (_T1 < _T20)
    if (_T21 == 0) branch _L16
    _T22 = 0
    _T23 = (_T1 < _T22)
    if (_T23 == 0) branch _L17
_L16:
    _T24 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T24
    call _PrintString
    call _Halt
_L17:
    _T25 = 4
    _T26 = (_T1 * _T25)
    _T27 = (_T26 + _T25)
    _T28 = *(_T0 + _T27)
    parm _T18
    parm _T28
    _T29 = *(_T18 + 0)
    _T30 = *(_T29 + 8)
    call _T30
    return _T18
_L15:
    _T32 = (_T1 + _T2)
    _T33 = 1
    _T34 = (_T32 + _T33)
    _T35 = 2
    _T36 = 0
    _T37 = (_T35 == _T36)
    if (_T37 == 0) branch _L18
    _T38 = "Decaf runtime error: Division by zero error."
    parm _T38
    call _PrintString
    call _Halt
_L18:
    _T39 = (_T34 / _T35)
    _T31 = _T39
    parm _T0
    parm _T1
    parm _T31
    _T41 =  call _Main.sort
    _T40 = _T41
    parm _T0
    parm _T31
    parm _T2
    _T42 =  call _Main.sort
    parm _T40
    parm _T42
    _T43 = *(_T40 + 0)
    _T44 = *(_T43 + 16)
    call _T44
    parm _T40
    _T45 = *(_T40 + 0)
    _T46 = *(_T45 + 12)
    call _T46
    return _T40
}

FUNCTION(main) {
memo ''
main:
    _T49 = 100
    _T48 = _T49
    _T50 = 0
    _T51 = (_T48 < _T50)
    if (_T51 == 0) branch _L19
    _T52 = "Decaf runtime error: Cannot create negative-sized array\n"
    parm _T52
    call _PrintString
    call _Halt
_L19:
    _T53 = 4
    _T54 = (_T53 * _T48)
    _T55 = (_T53 + _T54)
    parm _T55
    _T56 =  call _Alloc
    *(_T56 + 0) = _T48
    _T47 = _T56
    _T58 = 0
    _T57 = _T58
_L20:
    _T59 = (_T57 < _T48)
    if (_T59 == 0) branch _L21
    _T60 = *(_T47 + 0)
    _T61 = (_T57 < _T60)
    if (_T61 == 0) branch _L22
    _T62 = 0
    _T63 = (_T57 < _T62)
    if (_T63 == 0) branch _L23
_L22:
    _T64 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T64
    call _PrintString
    call _Halt
_L23:
    _T65 = 4
    _T66 = (_T57 * _T65)
    _T67 = (_T66 + _T65)
    _T68 = *(_T47 + _T67)
    _T69 = 4
    _T70 = (_T57 * _T69)
    _T71 = (_T70 + _T69)
    *(_T47 + _T71) = _T57
    _T72 = 1
    _T73 = (_T57 + _T72)
    _T57 = _T73
    branch _L20
_L21:
    _T75 = 0
    parm _T47
    parm _T75
    parm _T48
    _T76 =  call _Main.sort
    _T74 = _T76
    parm _T74
    _T77 = *(_T74 + 0)
    _T78 = *(_T77 + 12)
    call _T78
}

FUNCTION(_Sorted.init) {
memo '_T3:4 _T4:8'
_Sorted.init:
    _T79 = 1
    _T80 = 0
    _T81 = (_T79 < _T80)
    if (_T81 == 0) branch _L24
    _T82 = "Decaf runtime error: Cannot create negative-sized array\n"
    parm _T82
    call _PrintString
    call _Halt
_L24:
    _T83 = 4
    _T84 = (_T83 * _T79)
    _T85 = (_T83 + _T84)
    parm _T85
    _T86 =  call _Alloc
    *(_T86 + 0) = _T79
    _T87 = *(_T3 + 4)
    *(_T3 + 4) = _T86
    _T88 = *(_T3 + 4)
    _T89 = 0
    _T90 = *(_T88 + 0)
    _T91 = (_T89 < _T90)
    if (_T91 == 0) branch _L25
    _T92 = 0
    _T93 = (_T89 < _T92)
    if (_T93 == 0) branch _L26
_L25:
    _T94 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T94
    call _PrintString
    call _Halt
_L26:
    _T95 = 4
    _T96 = (_T89 * _T95)
    _T97 = (_T96 + _T95)
    _T98 = *(_T88 + _T97)
    _T99 = 4
    _T100 = (_T89 * _T99)
    _T101 = (_T100 + _T99)
    *(_T88 + _T101) = _T4
    _T102 = 1
    _T103 = *(_T3 + 8)
    *(_T3 + 8) = _T102
}

FUNCTION(_Sorted.print) {
memo '_T5:4'
_Sorted.print:
    _T105 = 0
    _T104 = _T105
_L27:
    _T106 = *(_T5 + 8)
    _T107 = (_T104 < _T106)
    if (_T107 == 0) branch _L28
    _T108 = *(_T5 + 4)
    _T109 = *(_T108 + 0)
    _T110 = (_T104 < _T109)
    if (_T110 == 0) branch _L29
    _T111 = 0
    _T112 = (_T104 < _T111)
    if (_T112 == 0) branch _L30
_L29:
    _T113 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T113
    call _PrintString
    call _Halt
_L30:
    _T114 = 4
    _T115 = (_T104 * _T114)
    _T116 = (_T115 + _T114)
    _T117 = *(_T108 + _T116)
    parm _T117
    call _PrintInt
    _T118 = " "
    parm _T118
    call _PrintString
    _T119 = 1
    _T120 = (_T104 + _T119)
    _T104 = _T120
    branch _L27
_L28:
    _T121 = "\n"
    parm _T121
    call _PrintString
}

FUNCTION(_Sorted.merge) {
memo '_T6:4 _T7:8'
_Sorted.merge:
    _T123 = *(_T6 + 8)
    _T124 = *(_T7 + 8)
    _T125 = (_T123 + _T124)
    _T126 = 0
    _T127 = (_T125 < _T126)
    if (_T127 == 0) branch _L31
    _T128 = "Decaf runtime error: Cannot create negative-sized array\n"
    parm _T128
    call _PrintString
    call _Halt
_L31:
    _T129 = 4
    _T130 = (_T129 * _T125)
    _T131 = (_T129 + _T130)
    parm _T131
    _T132 =  call _Alloc
    *(_T132 + 0) = _T125
    _T122 = _T132
    _T135 = 0
    _T133 = _T135
    _T136 = 0
    _T134 = _T136
_L32:
    _T137 = (_T133 + _T134)
    _T138 = *(_T6 + 8)
    _T139 = *(_T7 + 8)
    _T140 = (_T138 + _T139)
    _T141 = (_T137 < _T140)
    if (_T141 == 0) branch _L33
    _T142 = *(_T6 + 8)
    _T143 = (_T133 == _T142)
    if (_T143 == 0) branch _L34
    _T144 = *(_T7 + 4)
    _T145 = *(_T144 + 0)
    _T146 = (_T134 < _T145)
    if (_T146 == 0) branch _L35
    _T147 = 0
    _T148 = (_T134 < _T147)
    if (_T148 == 0) branch _L36
_L35:
    _T149 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T149
    call _PrintString
    call _Halt
_L36:
    _T150 = 4
    _T151 = (_T134 * _T150)
    _T152 = (_T151 + _T150)
    _T153 = *(_T144 + _T152)
    _T154 = (_T133 + _T134)
    _T155 = *(_T122 + 0)
    _T156 = (_T154 < _T155)
    if (_T156 == 0) branch _L37
    _T157 = 0
    _T158 = (_T154 < _T157)
    if (_T158 == 0) branch _L38
_L37:
    _T159 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T159
    call _PrintString
    call _Halt
_L38:
    _T160 = 4
    _T161 = (_T154 * _T160)
    _T162 = (_T161 + _T160)
    _T163 = *(_T122 + _T162)
    _T164 = 4
    _T165 = (_T154 * _T164)
    _T166 = (_T165 + _T164)
    *(_T122 + _T166) = _T153
    _T167 = 1
    _T168 = (_T134 + _T167)
    _T134 = _T168
    branch _L39
_L34:
    _T169 = *(_T7 + 8)
    _T170 = (_T134 == _T169)
    if (_T170 == 0) branch _L40
    _T171 = *(_T6 + 4)
    _T172 = *(_T171 + 0)
    _T173 = (_T133 < _T172)
    if (_T173 == 0) branch _L41
    _T174 = 0
    _T175 = (_T133 < _T174)
    if (_T175 == 0) branch _L42
_L41:
    _T176 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T176
    call _PrintString
    call _Halt
_L42:
    _T177 = 4
    _T178 = (_T133 * _T177)
    _T179 = (_T178 + _T177)
    _T180 = *(_T171 + _T179)
    _T181 = (_T133 + _T134)
    _T182 = *(_T122 + 0)
    _T183 = (_T181 < _T182)
    if (_T183 == 0) branch _L43
    _T184 = 0
    _T185 = (_T181 < _T184)
    if (_T185 == 0) branch _L44
_L43:
    _T186 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T186
    call _PrintString
    call _Halt
_L44:
    _T187 = 4
    _T188 = (_T181 * _T187)
    _T189 = (_T188 + _T187)
    _T190 = *(_T122 + _T189)
    _T191 = 4
    _T192 = (_T181 * _T191)
    _T193 = (_T192 + _T191)
    *(_T122 + _T193) = _T180
    _T194 = 1
    _T195 = (_T133 + _T194)
    _T133 = _T195
    branch _L45
_L40:
    _T196 = *(_T6 + 4)
    _T197 = *(_T196 + 0)
    _T198 = (_T133 < _T197)
    if (_T198 == 0) branch _L46
    _T199 = 0
    _T200 = (_T133 < _T199)
    if (_T200 == 0) branch _L47
_L46:
    _T201 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T201
    call _PrintString
    call _Halt
_L47:
    _T202 = 4
    _T203 = (_T133 * _T202)
    _T204 = (_T203 + _T202)
    _T205 = *(_T196 + _T204)
    _T206 = *(_T7 + 4)
    _T207 = *(_T206 + 0)
    _T208 = (_T134 < _T207)
    if (_T208 == 0) branch _L48
    _T209 = 0
    _T210 = (_T134 < _T209)
    if (_T210 == 0) branch _L49
_L48:
    _T211 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T211
    call _PrintString
    call _Halt
_L49:
    _T212 = 4
    _T213 = (_T134 * _T212)
    _T214 = (_T213 + _T212)
    _T215 = *(_T206 + _T214)
    _T216 = (_T205 < _T215)
    if (_T216 == 0) branch _L50
    _T217 = *(_T7 + 4)
    _T218 = *(_T217 + 0)
    _T219 = (_T134 < _T218)
    if (_T219 == 0) branch _L51
    _T220 = 0
    _T221 = (_T134 < _T220)
    if (_T221 == 0) branch _L52
_L51:
    _T222 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T222
    call _PrintString
    call _Halt
_L52:
    _T223 = 4
    _T224 = (_T134 * _T223)
    _T225 = (_T224 + _T223)
    _T226 = *(_T217 + _T225)
    _T227 = (_T133 + _T134)
    _T228 = *(_T122 + 0)
    _T229 = (_T227 < _T228)
    if (_T229 == 0) branch _L53
    _T230 = 0
    _T231 = (_T227 < _T230)
    if (_T231 == 0) branch _L54
_L53:
    _T232 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T232
    call _PrintString
    call _Halt
_L54:
    _T233 = 4
    _T234 = (_T227 * _T233)
    _T235 = (_T234 + _T233)
    _T236 = *(_T122 + _T235)
    _T237 = 4
    _T238 = (_T227 * _T237)
    _T239 = (_T238 + _T237)
    *(_T122 + _T239) = _T226
    _T240 = 1
    _T241 = (_T134 + _T240)
    _T134 = _T241
    branch _L55
_L50:
    _T242 = *(_T6 + 4)
    _T243 = *(_T242 + 0)
    _T244 = (_T133 < _T243)
    if (_T244 == 0) branch _L56
    _T245 = 0
    _T246 = (_T133 < _T245)
    if (_T246 == 0) branch _L57
_L56:
    _T247 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T247
    call _PrintString
    call _Halt
_L57:
    _T248 = 4
    _T249 = (_T133 * _T248)
    _T250 = (_T249 + _T248)
    _T251 = *(_T242 + _T250)
    _T252 = (_T133 + _T134)
    _T253 = *(_T122 + 0)
    _T254 = (_T252 < _T253)
    if (_T254 == 0) branch _L58
    _T255 = 0
    _T256 = (_T252 < _T255)
    if (_T256 == 0) branch _L59
_L58:
    _T257 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T257
    call _PrintString
    call _Halt
_L59:
    _T258 = 4
    _T259 = (_T252 * _T258)
    _T260 = (_T259 + _T258)
    _T261 = *(_T122 + _T260)
    _T262 = 4
    _T263 = (_T252 * _T262)
    _T264 = (_T263 + _T262)
    *(_T122 + _T264) = _T251
    _T265 = 1
    _T266 = (_T133 + _T265)
    _T133 = _T266
_L55:
_L45:
_L39:
    branch _L32
_L33:
    _T267 = *(_T6 + 4)
    *(_T6 + 4) = _T122
    _T268 = *(_T6 + 8)
    _T269 = *(_T7 + 8)
    _T270 = (_T268 + _T269)
    _T271 = *(_T6 + 8)
    *(_T6 + 8) = _T270
}

