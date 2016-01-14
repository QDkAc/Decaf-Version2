VTABLE(_Splay) {
    <empty>
    Splay
    _Splay.rightRotate;
    _Splay.leftRotate;
    _Splay.splay;
    _Splay.insert;
    _Splay.remove;
    _Splay.findMax;
}

VTABLE(_Main) {
    <empty>
    Main
}

VTABLE(_Node) {
    <empty>
    Node
    _Node.setArray;
    _Node.getL;
    _Node.getR;
    _Node.getP;
    _Node.setL;
    _Node.setR;
    _Node.setP;
    _Node.getSize;
    _Node.insert;
    _Node.find;
    _Node.findMax;
    _Node.rightRotate;
    _Node.leftRotate;
}

FUNCTION(_Splay_New) {
memo ''
_Splay_New:
    _T30 = 8
    parm _T30
    _T31 =  call _Alloc
    _T32 = VTBL <_Splay>
    *(_T31 + 0) = _T32
    return _T31
}

FUNCTION(_Main_New) {
memo ''
_Main_New:
    _T33 = 4
    parm _T33
    _T34 =  call _Alloc
    _T35 = VTBL <_Main>
    *(_T34 + 0) = _T35
    return _T34
}

FUNCTION(_Node_New) {
memo ''
_Node_New:
    _T36 = 24
    parm _T36
    _T37 =  call _Alloc
    _T38 = VTBL <_Node>
    *(_T37 + 0) = _T38
    return _T37
}

FUNCTION(_Splay.rightRotate) {
memo '_T0:4 _T1:8'
_Splay.rightRotate:
    parm _T1
    _T40 = *(_T1 + 0)
    _T41 = *(_T40 + 52)
    _T42 =  call _T41
    _T39 = _T42
    _T43 = *(_T0 + 4)
    _T44 = (_T43 == _T39)
    if (_T44 == 0) branch _L31
    _T45 = *(_T0 + 4)
    *(_T0 + 4) = _T1
_L31:
}

FUNCTION(_Splay.leftRotate) {
memo '_T2:4 _T3:8'
_Splay.leftRotate:
    parm _T3
    _T47 = *(_T3 + 0)
    _T48 = *(_T47 + 56)
    _T49 =  call _T48
    _T46 = _T49
    _T50 = *(_T2 + 4)
    _T51 = (_T50 == _T46)
    if (_T51 == 0) branch _L32
    _T52 = *(_T2 + 4)
    *(_T2 + 4) = _T3
_L32:
}

FUNCTION(_Splay.splay) {
memo '_T4:4 _T5:8'
_Splay.splay:
_L33:
    _T53 = *(_T4 + 4)
    _T54 = (_T5 != _T53)
    if (_T54 == 0) branch _L34
    parm _T5
    _T55 = *(_T5 + 0)
    _T56 = *(_T55 + 20)
    _T57 =  call _T56
    _T58 = *(_T4 + 4)
    _T59 = (_T57 == _T58)
    if (_T59 == 0) branch _L35
    _T60 = *(_T4 + 4)
    parm _T60
    _T61 = *(_T60 + 0)
    _T62 = *(_T61 + 12)
    _T63 =  call _T62
    _T64 = (_T63 == _T5)
    if (_T64 == 0) branch _L36
    parm _T4
    parm _T5
    _T65 = *(_T4 + 0)
    _T66 = *(_T65 + 8)
    call _T66
    branch _L37
_L36:
    parm _T4
    parm _T5
    _T67 = *(_T4 + 0)
    _T68 = *(_T67 + 12)
    call _T68
_L37:
    branch _L38
_L35:
    parm _T5
    _T71 = *(_T5 + 0)
    _T72 = *(_T71 + 20)
    _T73 =  call _T72
    _T69 = _T73
    parm _T69
    _T74 = *(_T69 + 0)
    _T75 = *(_T74 + 20)
    _T76 =  call _T75
    _T70 = _T76
    parm _T70
    _T77 = *(_T70 + 0)
    _T78 = *(_T77 + 12)
    _T79 =  call _T78
    _T80 = (_T79 == _T69)
    if (_T80 == 0) branch _L39
    parm _T69
    _T81 = *(_T69 + 0)
    _T82 = *(_T81 + 12)
    _T83 =  call _T82
    _T84 = (_T83 == _T5)
    if (_T84 == 0) branch _L40
    parm _T4
    parm _T69
    _T85 = *(_T4 + 0)
    _T86 = *(_T85 + 8)
    call _T86
    branch _L41
_L40:
    parm _T4
    parm _T5
    _T87 = *(_T4 + 0)
    _T88 = *(_T87 + 12)
    call _T88
_L41:
    parm _T4
    parm _T5
    _T89 = *(_T4 + 0)
    _T90 = *(_T89 + 8)
    call _T90
    branch _L42
_L39:
    parm _T69
    _T91 = *(_T69 + 0)
    _T92 = *(_T91 + 16)
    _T93 =  call _T92
    _T94 = (_T93 == _T5)
    if (_T94 == 0) branch _L43
    parm _T4
    parm _T69
    _T95 = *(_T4 + 0)
    _T96 = *(_T95 + 12)
    call _T96
    branch _L44
_L43:
    parm _T4
    parm _T5
    _T97 = *(_T4 + 0)
    _T98 = *(_T97 + 8)
    call _T98
_L44:
    parm _T4
    parm _T5
    _T99 = *(_T4 + 0)
    _T100 = *(_T99 + 12)
    call _T100
_L42:
_L38:
    branch _L33
_L34:
}

FUNCTION(_Splay.insert) {
memo '_T6:4 _T7:8'
_Splay.insert:
    _T101 = *(_T6 + 4)
    _T102 = 0
    _T103 = (_T101 == _T102)
    if (_T103 == 0) branch _L45
    _T104 =  call _Node_New
    _T105 = *(_T6 + 4)
    *(_T6 + 4) = _T104
    _T106 = *(_T6 + 4)
    parm _T106
    parm _T7
    _T107 = *(_T106 + 0)
    _T108 = *(_T107 + 8)
    call _T108
    branch _L46
_L45:
    _T110 = *(_T6 + 4)
    parm _T110
    parm _T7
    _T111 = *(_T110 + 0)
    _T112 = *(_T111 + 40)
    _T113 =  call _T112
    _T109 = _T113
    parm _T6
    parm _T109
    _T114 = *(_T6 + 0)
    _T115 = *(_T114 + 16)
    call _T115
_L46:
}

FUNCTION(_Splay.remove) {
memo '_T8:4 _T9:8'
_Splay.remove:
    _T117 = *(_T8 + 4)
    parm _T117
    parm _T9
    _T118 = *(_T117 + 0)
    _T119 = *(_T118 + 44)
    _T120 =  call _T119
    _T116 = _T120
    parm _T8
    parm _T116
    _T121 = *(_T8 + 0)
    _T122 = *(_T121 + 16)
    call _T122
    _T123 = *(_T8 + 4)
    parm _T123
    _T124 = *(_T123 + 0)
    _T125 = *(_T124 + 12)
    _T126 =  call _T125
    _T127 = 0
    _T128 = (_T126 == _T127)
    if (_T128 == 0) branch _L47
    _T129 = *(_T8 + 4)
    parm _T129
    _T130 = *(_T129 + 0)
    _T131 = *(_T130 + 16)
    _T132 =  call _T131
    _T133 = *(_T8 + 4)
    *(_T8 + 4) = _T132
    _T134 = *(_T8 + 4)
    _T135 = 0
    _T136 = (_T134 != _T135)
    if (_T136 == 0) branch _L48
    _T137 = *(_T8 + 4)
    _T138 = 0
    parm _T137
    parm _T138
    _T139 = *(_T137 + 0)
    _T140 = *(_T139 + 32)
    call _T140
_L48:
    branch _L49
_L47:
    _T141 = *(_T8 + 4)
    parm _T141
    _T142 = *(_T141 + 0)
    _T143 = *(_T142 + 16)
    _T144 =  call _T143
    _T116 = _T144
    _T145 = *(_T8 + 4)
    parm _T145
    _T146 = *(_T145 + 0)
    _T147 = *(_T146 + 12)
    _T148 =  call _T147
    _T149 = *(_T8 + 4)
    *(_T8 + 4) = _T148
    _T150 = *(_T8 + 4)
    _T151 = 0
    parm _T150
    parm _T151
    _T152 = *(_T150 + 0)
    _T153 = *(_T152 + 32)
    call _T153
    _T155 = *(_T8 + 4)
    parm _T155
    _T156 = *(_T155 + 0)
    _T157 = *(_T156 + 48)
    _T158 =  call _T157
    _T154 = _T158
    parm _T8
    parm _T154
    _T159 = *(_T8 + 0)
    _T160 = *(_T159 + 16)
    call _T160
    _T161 = 0
    _T162 = (_T116 != _T161)
    if (_T162 == 0) branch _L50
    _T163 = *(_T8 + 4)
    parm _T163
    parm _T116
    _T164 = *(_T163 + 0)
    _T165 = *(_T164 + 28)
    call _T165
    _T166 = *(_T8 + 4)
    parm _T116
    parm _T166
    _T167 = *(_T116 + 0)
    _T168 = *(_T167 + 32)
    call _T168
_L50:
_L49:
}

FUNCTION(_Splay.findMax) {
memo '_T10:4'
_Splay.findMax:
    _T169 = *(_T10 + 4)
    parm _T169
    _T170 = *(_T169 + 0)
    _T171 = *(_T170 + 48)
    _T172 =  call _T171
    parm _T172
    _T173 = *(_T172 + 0)
    _T174 = *(_T173 + 36)
    _T175 =  call _T174
    return _T175
}

FUNCTION(main) {
memo ''
main:
    _T177 =  call _Splay_New
    _T176 = _T177
    _T178 = 100
    parm _T176
    parm _T178
    _T179 = *(_T176 + 0)
    _T180 = *(_T179 + 20)
    call _T180
    _T181 = 50
    parm _T176
    parm _T181
    _T182 = *(_T176 + 0)
    _T183 = *(_T182 + 20)
    call _T183
    _T184 = 70
    parm _T176
    parm _T184
    _T185 = *(_T176 + 0)
    _T186 = *(_T185 + 20)
    call _T186
    _T187 = 100
    parm _T176
    parm _T187
    _T188 = *(_T176 + 0)
    _T189 = *(_T188 + 24)
    call _T189
    parm _T176
    _T190 = *(_T176 + 0)
    _T191 = *(_T190 + 28)
    _T192 =  call _T191
    parm _T192
    call _PrintInt
}

FUNCTION(_Node.setArray) {
memo '_T11:4 _T12:8'
_Node.setArray:
    _T193 = 0
    _T194 = (_T12 < _T193)
    if (_T194 == 0) branch _L51
    _T195 = "Decaf runtime error: Cannot create negative-sized array\n"
    parm _T195
    call _PrintString
    call _Halt
_L51:
    _T196 = 4
    _T197 = (_T196 * _T12)
    _T198 = (_T196 + _T197)
    parm _T198
    _T199 =  call _Alloc
    *(_T199 + 0) = _T12
    _T200 = *(_T11 + 16)
    *(_T11 + 16) = _T199
    _T201 = *(_T11 + 20)
    *(_T11 + 20) = _T12
}

FUNCTION(_Node.getL) {
memo '_T13:4'
_Node.getL:
    _T202 = *(_T13 + 4)
    return _T202
}

FUNCTION(_Node.getR) {
memo '_T14:4'
_Node.getR:
    _T203 = *(_T14 + 8)
    return _T203
}

FUNCTION(_Node.getP) {
memo '_T15:4'
_Node.getP:
    _T204 = *(_T15 + 12)
    return _T204
}

FUNCTION(_Node.setL) {
memo '_T16:4 _T17:8'
_Node.setL:
    _T205 = *(_T16 + 4)
    *(_T16 + 4) = _T17
}

FUNCTION(_Node.setR) {
memo '_T18:4 _T19:8'
_Node.setR:
    _T206 = *(_T18 + 8)
    *(_T18 + 8) = _T19
}

FUNCTION(_Node.setP) {
memo '_T20:4 _T21:8'
_Node.setP:
    _T207 = *(_T20 + 12)
    *(_T20 + 12) = _T21
}

FUNCTION(_Node.getSize) {
memo '_T22:4'
_Node.getSize:
    _T208 = *(_T22 + 20)
    return _T208
}

FUNCTION(_Node.insert) {
memo '_T23:4 _T24:8'
_Node.insert:
    _T209 = *(_T23 + 20)
    _T210 = (_T24 < _T209)
    if (_T210 == 0) branch _L52
    _T211 = *(_T23 + 4)
    _T212 = 0
    _T213 = (_T211 == _T212)
    if (_T213 == 0) branch _L53
    _T214 =  call _Node_New
    _T215 = *(_T23 + 4)
    *(_T23 + 4) = _T214
    _T216 = *(_T23 + 4)
    parm _T216
    parm _T24
    _T217 = *(_T216 + 0)
    _T218 = *(_T217 + 8)
    call _T218
    _T219 = *(_T23 + 4)
    _T220 = *(_T219 + 12)
    *(_T219 + 12) = _T23
    _T221 = *(_T23 + 4)
    return _T221
    branch _L54
_L53:
    _T222 = *(_T23 + 4)
    parm _T222
    parm _T24
    _T223 = *(_T222 + 0)
    _T224 = *(_T223 + 40)
    _T225 =  call _T224
    return _T225
_L54:
    branch _L55
_L52:
    _T226 = *(_T23 + 8)
    _T227 = 0
    _T228 = (_T226 == _T227)
    if (_T228 == 0) branch _L56
    _T229 =  call _Node_New
    _T230 = *(_T23 + 8)
    *(_T23 + 8) = _T229
    _T231 = *(_T23 + 8)
    parm _T231
    parm _T24
    _T232 = *(_T231 + 0)
    _T233 = *(_T232 + 8)
    call _T233
    _T234 = *(_T23 + 8)
    _T235 = *(_T234 + 12)
    *(_T234 + 12) = _T23
    _T236 = *(_T23 + 8)
    return _T236
    branch _L57
_L56:
    _T237 = *(_T23 + 8)
    parm _T237
    parm _T24
    _T238 = *(_T237 + 0)
    _T239 = *(_T238 + 40)
    _T240 =  call _T239
    return _T240
_L57:
_L55:
}

FUNCTION(_Node.find) {
memo '_T25:4 _T26:8'
_Node.find:
    _T241 = *(_T25 + 20)
    _T242 = (_T26 == _T241)
    if (_T242 == 0) branch _L58
    return _T25
_L58:
    _T243 = *(_T25 + 20)
    _T244 = (_T26 < _T243)
    if (_T244 == 0) branch _L59
    _T245 = *(_T25 + 4)
    _T246 = 0
    _T247 = (_T245 == _T246)
    if (_T247 == 0) branch _L60
    _T248 = "Failed"
    parm _T248
    call _PrintString
    _T249 = 0
    return _T249
    branch _L61
_L60:
    _T250 = *(_T25 + 4)
    parm _T250
    parm _T26
    _T251 = *(_T250 + 0)
    _T252 = *(_T251 + 44)
    _T253 =  call _T252
    return _T253
_L61:
    branch _L62
_L59:
    _T254 = *(_T25 + 8)
    _T255 = 0
    _T256 = (_T254 == _T255)
    if (_T256 == 0) branch _L63
    _T257 = "Failed"
    parm _T257
    call _PrintString
    _T258 = 0
    return _T258
    branch _L64
_L63:
    _T259 = *(_T25 + 8)
    parm _T259
    parm _T26
    _T260 = *(_T259 + 0)
    _T261 = *(_T260 + 44)
    _T262 =  call _T261
    return _T262
_L64:
_L62:
}

FUNCTION(_Node.findMax) {
memo '_T27:4'
_Node.findMax:
    _T263 = *(_T27 + 8)
    _T264 = 0
    _T265 = (_T263 == _T264)
    if (_T265 == 0) branch _L65
    return _T27
    branch _L66
_L65:
    _T266 = *(_T27 + 8)
    parm _T266
    _T267 = *(_T266 + 0)
    _T268 = *(_T267 + 48)
    _T269 =  call _T268
    return _T269
_L66:
}

FUNCTION(_Node.rightRotate) {
memo '_T28:4'
_Node.rightRotate:
    _T271 = *(_T28 + 12)
    _T270 = _T271
    _T272 = *(_T28 + 8)
    _T273 = *(_T270 + 4)
    *(_T270 + 4) = _T272
    _T274 = *(_T28 + 8)
    _T275 = 0
    _T276 = (_T274 != _T275)
    if (_T276 == 0) branch _L67
    _T277 = *(_T28 + 8)
    _T278 = *(_T277 + 12)
    *(_T277 + 12) = _T270
_L67:
    _T279 = *(_T270 + 12)
    _T280 = *(_T28 + 12)
    *(_T28 + 12) = _T279
    _T281 = *(_T270 + 12)
    _T282 = 0
    _T283 = (_T281 != _T282)
    if (_T283 == 0) branch _L68
    _T284 = *(_T270 + 12)
    _T285 = *(_T284 + 4)
    _T286 = (_T285 == _T270)
    if (_T286 == 0) branch _L69
    _T287 = *(_T270 + 12)
    _T288 = *(_T287 + 4)
    *(_T287 + 4) = _T28
    branch _L70
_L69:
    _T289 = *(_T270 + 12)
    _T290 = *(_T289 + 8)
    *(_T289 + 8) = _T28
_L70:
_L68:
    _T291 = *(_T28 + 8)
    *(_T28 + 8) = _T270
    _T292 = *(_T270 + 12)
    *(_T270 + 12) = _T28
    return _T270
}

FUNCTION(_Node.leftRotate) {
memo '_T29:4'
_Node.leftRotate:
    _T294 = *(_T29 + 12)
    _T293 = _T294
    _T295 = *(_T29 + 4)
    _T296 = *(_T293 + 8)
    *(_T293 + 8) = _T295
    _T297 = *(_T29 + 4)
    _T298 = 0
    _T299 = (_T297 != _T298)
    if (_T299 == 0) branch _L71
    _T300 = *(_T29 + 4)
    _T301 = *(_T300 + 12)
    *(_T300 + 12) = _T293
_L71:
    _T302 = *(_T293 + 12)
    _T303 = *(_T29 + 12)
    *(_T29 + 12) = _T302
    _T304 = *(_T293 + 12)
    _T305 = 0
    _T306 = (_T304 != _T305)
    if (_T306 == 0) branch _L72
    _T307 = *(_T293 + 12)
    _T308 = *(_T307 + 4)
    _T309 = (_T308 == _T293)
    if (_T309 == 0) branch _L73
    _T310 = *(_T293 + 12)
    _T311 = *(_T310 + 4)
    *(_T310 + 4) = _T29
    branch _L74
_L73:
    _T312 = *(_T293 + 12)
    _T313 = *(_T312 + 8)
    *(_T312 + 8) = _T29
_L74:
_L72:
    _T314 = *(_T29 + 4)
    *(_T29 + 4) = _T293
    _T315 = *(_T293 + 12)
    *(_T293 + 12) = _T29
    return _T293
}

