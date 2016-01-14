VTABLE(_Main) {
    <empty>
    Main
}

VTABLE(_Item) {
    <empty>
    Item
    _Item.setId;
    _Item.printId;
}

FUNCTION(_Main_New) {
memo ''
_Main_New:
    _T3 = 4
    parm _T3
    _T4 =  call _Alloc
    _T5 = VTBL <_Main>
    *(_T4 + 0) = _T5
    return _T4
}

FUNCTION(_Item_New) {
memo ''
_Item_New:
    _T6 = 8
    parm _T6
    _T7 =  call _Alloc
    _T8 = VTBL <_Item>
    *(_T7 + 0) = _T8
    return _T7
}

FUNCTION(main) {
memo ''
main:
    _T10 = 0
    _T9 = _T10
_L13:
    _T12 = 10
    _T13 = (_T9 < _T12)
    if (_T13 == 0) branch _L14
    _T14 =  call _Item_New
    _T11 = _T14
    parm _T11
    parm _T9
    _T15 = *(_T11 + 0)
    _T16 = *(_T15 + 8)
    call _T16
    parm _T11
    _T17 = *(_T11 + 0)
    _T18 = *(_T17 + 12)
    call _T18
    _T19 = 1
    _T20 = (_T9 + _T19)
    _T9 = _T20
    branch _L13
_L14:
}

FUNCTION(_Item.setId) {
memo '_T0:4 _T1:8'
_Item.setId:
    _T21 = *(_T0 + 4)
    *(_T0 + 4) = _T1
}

FUNCTION(_Item.printId) {
memo '_T2:4'
_Item.printId:
    _T22 = *(_T2 + 4)
    parm _T22
    call _PrintInt
    _T23 = "\n"
    parm _T23
    call _PrintString
}

