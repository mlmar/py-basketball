import type { ContainerProps } from '@/components/types/ContainerProps';
import { css } from '@/util/css';

interface HeroProps extends ContainerProps {}

export function Hero({ className, ...rest }: HeroProps) {
    return <header className={css('hero', className)} {...rest}></header>;
}

interface HeroCardProps extends ContainerProps {}

Hero.Card = function ({ className, ...rest }: HeroCardProps) {
    return <article className={css('hero-card', className)} {...rest}></article>;
};

interface HeroButtonProps extends ContainerProps {}

Hero.Buttons = function ({ className, ...rest }: HeroButtonProps) {
    return <nav className={css('hero-buttons', className)} {...rest}></nav>;
};
