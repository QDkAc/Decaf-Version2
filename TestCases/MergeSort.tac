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
    return _T40
}

FUNCTION(main) {
memo ''
main:
    _T47 = 100
    _T46 = _T47
    _T48 = 0
    _T49 = (_T46 < _T48)
    if (_T49 == 0) branch _L19
    _T50 = "Decaf runtime error: Cannot create negative-sized array\n"
    parm _T50
    call _PrintString
    call _Halt
_L19:
    _T51 = 4
    _T52 = (_T51 * _T46)
    _T53 = (_T51 + _T52)
    parm _T53
    _T54 =  call _Alloc
    *(_T54 + 0) = _T46
    _T45 = _T54
    _T56 = 0
    _T55 = _T56
_L20:
    _T57 = (_T55 < _T46)
    if (_T57 == 0) branch _L21
    _T58 = *(_T45 + 0)
    _T59 = (_T55 < _T58)
    if (_T59 == 0) branch _L22
    _T60 = 0
    _T61 = (_T55 < _T60)
    if (_T61 == 0) branch _L23
_L22:
    _T62 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T62
    call _PrintString
    call _Halt
_L23:
    _T63 = 4
    _T64 = (_T55 * _T63)
    _T65 = (_T64 + _T63)
    _T66 = *(_T45 + _T65)
    _T67 = 4
    _T68 = (_T55 * _T67)
    _T69 = (_T68 + _T67)
    *(_T45 + _T69) = _T55
    _T70 = 1
    _T71 = (_T55 + _T70)
    _T55 = _T71
    branch _L20
_L21:
    _T73 = 0
    parm _T45
    parm _T73
    parm _T46
    _T74 =  call _Main.sort
    _T72 = _T74
    parm _T72
    _T75 = *(_T72 + 0)
    _T76 = *(_T75 + 12)
    call _T76
}

FUNCTION(_Sorted.init) {
memo '_T3:4 _T4:8'
_Sorted.init:
    _T77 = 1
    _T78 = 0
    _T79 = (_T77 < _T78)
    if (_T79 == 0) branch _L24
    _T80 = "Decaf runtime error: Cannot create negative-sized array\n"
    parm _T80
    call _PrintString
    call _Halt
_L24:
    _T81 = 4
    _T82 = (_T81 * _T77)
    _T83 = (_T81 + _T82)
    parm _T83
    _T84 =  call _Alloc
    *(_T84 + 0) = _T77
    _T85 = *(_T3 + 4)
    *(_T3 + 4) = _T84
    _T86 = *(_T3 + 4)
    _T87 = 0
    _T88 = *(_T86 + 0)
    _T89 = (_T87 < _T88)
    if (_T89 == 0) branch _L25
    _T90 = 0
    _T91 = (_T87 < _T90)
    if (_T91 == 0) branch _L26
_L25:
    _T92 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T92
    call _PrintString
    call _Halt
_L26:
    _T93 = 4
    _T94 = (_T87 * _T93)
    _T95 = (_T94 + _T93)
    _T96 = *(_T86 + _T95)
    _T97 = 4
    _T98 = (_T87 * _T97)
    _T99 = (_T98 + _T97)
    *(_T86 + _T99) = _T4
    _T100 = 1
    _T101 = *(_T3 + 8)
    *(_T3 + 8) = _T100
}

FUNCTION(_Sorted.print) {
memo '_T5:4'
_Sorted.print:
    _T103 = 0
    _T102 = _T103
_L27:
    _T104 = *(_T5 + 8)
    _T105 = (_T102 < _T104)
    if (_T105 == 0) branch _L28
    _T106 = *(_T5 + 4)
    _T107 = *(_T106 + 0)
    _T108 = (_T102 < _T107)
    if (_T108 == 0) branch _L29
    _T109 = 0
    _T110 = (_T102 < _T109)
    if (_T110 == 0) branch _L30
_L29:
    _T111 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T111
    call _PrintString
    call _Halt
_L30:
    _T112 = 4
    _T113 = (_T102 * _T112)
    _T114 = (_T113 + _T112)
    _T115 = *(_T106 + _T114)
    parm _T115
    call _PrintInt
    _T116 = " "
    parm _T116
    call _PrintString
    _T117 = 1
    _T118 = (_T102 + _T117)
    _T102 = _T118
    branch _L27
_L28:
    _T119 = "\n"
    parm _T119
    call _PrintString
}

FUNCTION(_Sorted.merge) {
memo '_T6:4 _T7:8'
_Sorted.merge:
    _T121 = *(_T6 + 8)
    _T122 = *(_T7 + 8)
    _T123 = (_T121 + _T122)
    _T124 = 0
    _T125 = (_T123 < _T124)
    if (_T125 == 0) branch _L31
    _T126 = "Decaf runtime error: Cannot create negative-sized array\n"
    parm _T126
    call _PrintString
    call _Halt
_L31:
    _T127 = 4
    _T128 = (_T127 * _T123)
    _T129 = (_T127 + _T128)
    parm _T129
    _T130 =  call _Alloc
    *(_T130 + 0) = _T123
    _T120 = _T130
    _T133 = 0
    _T131 = _T133
    _T134 = 0
    _T132 = _T134
_L32:
    _T135 = (_T131 + _T132)
    _T136 = *(_T6 + 8)
    _T137 = *(_T7 + 8)
    _T138 = (_T136 + _T137)
    _T139 = (_T135 < _T138)
    if (_T139 == 0) branch _L33
    _T140 = *(_T6 + 8)
    _T141 = (_T131 == _T140)
    if (_T141 == 0) branch _L34
    _T142 = *(_T7 + 4)
    _T143 = *(_T142 + 0)
    _T144 = (_T132 < _T143)
    if (_T144 == 0) branch _L35
    _T145 = 0
    _T146 = (_T132 < _T145)
    if (_T146 == 0) branch _L36
_L35:
    _T147 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T147
    call _PrintString
    call _Halt
_L36:
    _T148 = 4
    _T149 = (_T132 * _T148)
    _T150 = (_T149 + _T148)
    _T151 = *(_T142 + _T150)
    _T152 = (_T131 + _T132)
    _T153 = *(_T120 + 0)
    _T154 = (_T152 < _T153)
    if (_T154 == 0) branch _L37
    _T155 = 0
    _T156 = (_T152 < _T155)
    if (_T156 == 0) branch _L38
_L37:
    _T157 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T157
    call _PrintString
    call _Halt
_L38:
    _T158 = 4
    _T159 = (_T152 * _T158)
    _T160 = (_T159 + _T158)
    _T161 = *(_T120 + _T160)
    _T162 = 4
    _T163 = (_T152 * _T162)
    _T164 = (_T163 + _T162)
    *(_T120 + _T164) = _T151
    _T165 = 1
    _T166 = (_T132 + _T165)
    _T132 = _T166
    branch _L39
_L34:
    _T167 = *(_T7 + 8)
    _T168 = (_T132 == _T167)
    if (_T168 == 0) branch _L40
    _T169 = *(_T6 + 4)
    _T170 = *(_T169 + 0)
    _T171 = (_T131 < _T170)
    if (_T171 == 0) branch _L41
    _T172 = 0
    _T173 = (_T131 < _T172)
    if (_T173 == 0) branch _L42
_L41:
    _T174 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T174
    call _PrintString
    call _Halt
_L42:
    _T175 = 4
    _T176 = (_T131 * _T175)
    _T177 = (_T176 + _T175)
    _T178 = *(_T169 + _T177)
    _T179 = (_T131 + _T132)
    _T180 = *(_T120 + 0)
    _T181 = (_T179 < _T180)
    if (_T181 == 0) branch _L43
    _T182 = 0
    _T183 = (_T179 < _T182)
    if (_T183 == 0) branch _L44
_L43:
    _T184 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T184
    call _PrintString
    call _Halt
_L44:
    _T185 = 4
    _T186 = (_T179 * _T185)
    _T187 = (_T186 + _T185)
    _T188 = *(_T120 + _T187)
    _T189 = 4
    _T190 = (_T179 * _T189)
    _T191 = (_T190 + _T189)
    *(_T120 + _T191) = _T178
    _T192 = 1
    _T193 = (_T131 + _T192)
    _T131 = _T193
    branch _L45
_L40:
    _T194 = *(_T6 + 4)
    _T195 = *(_T194 + 0)
    _T196 = (_T131 < _T195)
    if (_T196 == 0) branch _L46
    _T197 = 0
    _T198 = (_T131 < _T197)
    if (_T198 == 0) branch _L47
_L46:
    _T199 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T199
    call _PrintString
    call _Halt
_L47:
    _T200 = 4
    _T201 = (_T131 * _T200)
    _T202 = (_T201 + _T200)
    _T203 = *(_T194 + _T202)
    _T204 = *(_T7 + 4)
    _T205 = *(_T204 + 0)
    _T206 = (_T132 < _T205)
    if (_T206 == 0) branch _L48
    _T207 = 0
    _T208 = (_T132 < _T207)
    if (_T208 == 0) branch _L49
_L48:
    _T209 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T209
    call _PrintString
    call _Halt
_L49:
    _T210 = 4
    _T211 = (_T132 * _T210)
    _T212 = (_T211 + _T210)
    _T213 = *(_T204 + _T212)
    _T214 = (_T203 < _T213)
    if (_T214 == 0) branch _L50
    _T215 = *(_T7 + 4)
    _T216 = *(_T215 + 0)
    _T217 = (_T132 < _T216)
    if (_T217 == 0) branch _L51
    _T218 = 0
    _T219 = (_T132 < _T218)
    if (_T219 == 0) branch _L52
_L51:
    _T220 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T220
    call _PrintString
    call _Halt
_L52:
    _T221 = 4
    _T222 = (_T132 * _T221)
    _T223 = (_T222 + _T221)
    _T224 = *(_T215 + _T223)
    _T225 = (_T131 + _T132)
    _T226 = *(_T120 + 0)
    _T227 = (_T225 < _T226)
    if (_T227 == 0) branch _L53
    _T228 = 0
    _T229 = (_T225 < _T228)
    if (_T229 == 0) branch _L54
_L53:
    _T230 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T230
    call _PrintString
    call _Halt
_L54:
    _T231 = 4
    _T232 = (_T225 * _T231)
    _T233 = (_T232 + _T231)
    _T234 = *(_T120 + _T233)
    _T235 = 4
    _T236 = (_T225 * _T235)
    _T237 = (_T236 + _T235)
    *(_T120 + _T237) = _T224
    _T238 = 1
    _T239 = (_T132 + _T238)
    _T132 = _T239
    branch _L55
_L50:
    _T240 = *(_T6 + 4)
    _T241 = *(_T240 + 0)
    _T242 = (_T131 < _T241)
    if (_T242 == 0) branch _L56
    _T243 = 0
    _T244 = (_T131 < _T243)
    if (_T244 == 0) branch _L57
_L56:
    _T245 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T245
    call _PrintString
    call _Halt
_L57:
    _T246 = 4
    _T247 = (_T131 * _T246)
    _T248 = (_T247 + _T246)
    _T249 = *(_T240 + _T248)
    _T250 = (_T131 + _T132)
    _T251 = *(_T120 + 0)
    _T252 = (_T250 < _T251)
    if (_T252 == 0) branch _L58
    _T253 = 0
    _T254 = (_T250 < _T253)
    if (_T254 == 0) branch _L59
_L58:
    _T255 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T255
    call _PrintString
    call _Halt
_L59:
    _T256 = 4
    _T257 = (_T250 * _T256)
    _T258 = (_T257 + _T256)
    _T259 = *(_T120 + _T258)
    _T260 = 4
    _T261 = (_T250 * _T260)
    _T262 = (_T261 + _T260)
    *(_T120 + _T262) = _T249
    _T263 = 1
    _T264 = (_T131 + _T263)
    _T131 = _T264
_L55:
_L45:
_L39:
    branch _L32
_L33:
    _T265 = *(_T6 + 4)
    *(_T6 + 4) = _T120
    _T266 = *(_T6 + 8)
    _T267 = *(_T7 + 8)
    _T268 = (_T266 + _T267)
    _T269 = *(_T6 + 8)
    *(_T6 + 8) = _T268
}

