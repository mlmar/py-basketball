import type { ContainerProps } from '@/components/types/ContainerProps';
import { css } from '@/util/css';

interface FooterProps extends ContainerProps {}

export function Footer({ className, ...rest }: FooterProps) {
    return <footer className={css('footer', className)} {...rest}></footer>;
}
