import type { ContainerProps } from '@/components/types/ContainerProps';
import { css } from '@/util/css';
import { Link } from '@tanstack/react-router';

export function BackButton({ className, children, ...rest }: ContainerProps) {
    return (
        <Link to='..'>
            <button id='back-btn' className={css('btn tiny back-btn', className)} {...rest}>
                ← {children}
            </button>
        </Link>
    );
}
