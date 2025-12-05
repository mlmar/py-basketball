import type { ContainerProps } from '@/components/types/ContainerProps';
import { css } from '@/util/css';

export function Hero({ className, ...rest }: ContainerProps) {
    return <header className={css('hero', className)} {...rest}></header>;
}

Hero.Card = function ({ className, ...rest }: ContainerProps) {
    return <article className={css('hero-card', className)} {...rest}></article>;
};

Hero.Buttons = function ({ className, ...rest }: ContainerProps) {
    return <nav className={css('hero-buttons', className)} {...rest}></nav>;
};
