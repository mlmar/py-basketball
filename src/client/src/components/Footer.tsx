import type { ContainerProps } from '@/components/types/ContainerProps';
import { css } from '@/util/css';

export function Footer({ className, ...rest }: ContainerProps) {
    return <footer className={css('footer', className)} {...rest}></footer>;
}
