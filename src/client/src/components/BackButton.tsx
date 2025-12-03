import type { ContainerProps } from '@/components/types/ContainerProps';
import { Link } from '@tanstack/react-router';

export function BackButton({ className, children, ...rest }: ContainerProps) {
    return (
        <Link to='..'>
            <button className='btn tiny'>← {children}</button>
        </Link>
    );
}
