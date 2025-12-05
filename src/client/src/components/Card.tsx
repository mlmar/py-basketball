import type { ContainerProps } from '@/components/types/ContainerProps';
import { css } from '@/util/css';

export function Card({ className, ...rest }: ContainerProps) {
    return <article className={css('card', className)} {...rest}></article>;
}

Card.Header = function ({ className, ...rest }: ContainerProps) {
    return <header className={css('card-header', className)} {...rest}></header>;
};

Card.Badge = function ({ className, ...rest }: ContainerProps) {
    return <span className={css('card-badge', className)} {...rest}></span>;
};

Card.Sub = function ({ className, ...rest }: ContainerProps) {
    return <p className={css('card-sub', className)} {...rest}></p>;
};
