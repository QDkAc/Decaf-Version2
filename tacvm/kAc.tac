VTABLE(_Main) {
    <empty>
    Main
}

FUNCTION(_Main_New) {
memo ''
_Main_New:
    _T0 = 4
    parm _T0
    _T1 =  call _Alloc
    _T2 = VTBL <_Main>
    *(_T1 + 0) = _T2
    return _T1
}

FUNCTION(_Main.func) {
memo ''
_Main.func:
	_T10 = 8
	parm _T10
	_T11 = call _Alloc
	parm _T10
	_T12 = call _Alloc
	*(_T11 + 0) = _T12
	*(_T11 + 4) = _T12
    	parm _T10
    	_T14 = call _Alloc
}

FUNCTION(main) {
memo ''
main:
    _T3 = 4
    parm _T3
    _T4 =  call _Alloc
    _T5 = "Start\n"
    parm _T5
    call _PrintString
    call _Main.func
    _T6 = "End\n"
    parm _T6
    call _PrintString
    call _GC

}

