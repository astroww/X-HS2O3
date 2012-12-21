        PROGRAM test_getarg
c        INTEGER :: i
        CHARACTER(len=32) :: arg
c        DO i = 1, iargc()
c        m=iargc()
c        CALL getarg(0, arg)
        CALL getarg(1, arg)
c        print *, m
        WRITE(*,*) arg
c        END DO
c       add testing sentence
        END PROGRAM
