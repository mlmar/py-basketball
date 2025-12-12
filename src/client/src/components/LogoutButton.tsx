import type { ContainerProps } from '@/components/types/ContainerProps';
import { css } from '@/util/css';
import { Link } from '@tanstack/react-router';

export function LogoutButton({ className, ...rest }: ContainerProps) {
    return (
        <Link to='/logout'>
            <button id='back-btn' className={css('btn ghost logout-btn', className)} {...rest}>
                Logout
            </button>
        </Link>
    );
}
