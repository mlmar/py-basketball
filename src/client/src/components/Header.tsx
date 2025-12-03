import type { ContainerProps } from '@/components/types/ContainerProps';
import { css } from '@/util/css';

interface HeaderProps extends ContainerProps {}

export function Header({ className, ...rest }: HeaderProps) {
    return <header className={css('header', className)} {...rest}></header>;
}

Header.TopNav = function ({ className, ...rest }: ContainerProps) {
    return <nav className={css('top-nav flex flex-space-between', className)} {...rest}></nav>;
};

Header.Logo = function ({ className, ...rest }: ContainerProps) {
    return (
        <h1 className={css('logo', className)} {...rest}>
            WaiverWarrior
        </h1>
    );
};

Header.Subtext = function ({ className, ...rest }: ContainerProps) {
    return <p className={css('subtext', className)} {...rest}></p>;
};

Header.Tagline = function ({ className, ...rest }: ContainerProps) {
    return <p className={css('tagline', className)} {...rest}></p>;
};
