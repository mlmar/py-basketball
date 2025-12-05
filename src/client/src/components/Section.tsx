import type { ContainerProps } from '@/components/types/ContainerProps';
import { css } from '@/util/css';

export function Section({ className = '', ...rest }: ContainerProps) {
    return <section className={css('section', className)} {...rest}></section>;
}
