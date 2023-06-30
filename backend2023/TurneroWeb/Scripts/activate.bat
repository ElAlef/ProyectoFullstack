@set "VIRTUAL_ENV=C:\Users\Alejandro\Desktop\PROGRAMACION\01 ISPC\Programacion Web II\ProyectoIntegrador E-Commerce\backend2023\TurneroWeb"

@if defined _OLD_VIRTUAL_PROMPT (
    @set "PROMPT=%_OLD_VIRTUAL_PROMPT%"
) else (
    @if not defined PROMPT (
        @set "PROMPT=$P$G"
    )
    @if not defined VIRTUAL_ENV_DISABLE_PROMPT (
        @set "_OLD_VIRTUAL_PROMPT=%PROMPT%"
    )
)
@if not defined VIRTUAL_ENV_DISABLE_PROMPT (
    @if "" NEQ "" (
        @set "PROMPT=() %PROMPT%"
    ) else (
        @for %%d in ("%VIRTUAL_ENV%") do @set "PROMPT=(%%~nxd) %PROMPT%"
    )
)

<<<<<<< HEAD
set VIRTUAL_ENV=C:\Users\Asus\Desktop\ProyectoFullStack2023\ProyectoFullstack\backend2023\TurneroWeb
=======
@REM Don't use () to avoid problems with them in %PATH%
@if defined _OLD_VIRTUAL_PYTHONHOME @goto ENDIFVHOME
    @set "_OLD_VIRTUAL_PYTHONHOME=%PYTHONHOME%"
:ENDIFVHOME
>>>>>>> c0a4120cfd873d05c05e8f3c7afe104f5e02149a

@set PYTHONHOME=

@REM if defined _OLD_VIRTUAL_PATH (
@if not defined _OLD_VIRTUAL_PATH @goto ENDIFVPATH1
    @set "PATH=%_OLD_VIRTUAL_PATH%"
:ENDIFVPATH1
@REM ) else (
@if defined _OLD_VIRTUAL_PATH @goto ENDIFVPATH2
    @set "_OLD_VIRTUAL_PATH=%PATH%"
:ENDIFVPATH2

@set "PATH=%VIRTUAL_ENV%\Scripts;%PATH%"
