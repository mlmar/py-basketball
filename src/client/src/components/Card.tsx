import type { ContainerProps } from '@/components/types/ContainerProps';
import { css } from '@/util/css';

interface CardProps extends ContainerProps {}

export function Card({ className, ...rest }: CardProps) {
    return <article className={css('card', className)} {...rest}></article>;
}

interface CardHeaderProps extends ContainerProps {}

Card.Header = function ({ className, ...rest }: CardHeaderProps) {
    return <header className={css('card-header', className)} {...rest}></header>;
};

interface CardBadgeProps extends ContainerProps {}

Card.Badge = function ({ className, ...rest }: CardBadgeProps) {
    return <span className={css('card-badge', className)} {...rest}></span>;
};
