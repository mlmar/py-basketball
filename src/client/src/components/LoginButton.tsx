import type { ContainerProps } from '@/components/types/ContainerProps';
import { css } from '@/util/css';
import { Link } from '@tanstack/react-router';

export function LoginButton({ className, ...rest }: ContainerProps) {
    return (
        <Link to='/login'>
            <button id='back-btn' className={css('btn ghost logout-btn', className)} {...rest}>
                Login
            </button>
        </Link>
    );
}
