module play
    implicit none

    contains

    ! Producto escalar entre dos vectores u, v de longitud n
    subroutine search(m, n, a, p)
        
        integer, intent(in), dimension(5,5) :: a
        integer, intent(in) :: n, m
        integer, intent(out) :: p
        !integer :: d
        
        write (*, *) "Good day, I am Fortran"
        p = a(m, n)
        write (*, *) "Fortran says ...Good Bye"
        
    end subroutine

    ! Producto vectorial entre dos vectores u, v de longitud 3
    function producto_vectorial(u, v) result(w)

        double precision, intent(in) :: u(3), v(3)
        double precision :: w(3)

        w(1) = u(2) * v(3) - u(3) * v(2)
        w(2) = u(3) * v(1) - u(1) * v(3)
        w(3) = u(1) * v(2) - u(2) * v(1)

    end function
    
end module