import type { ContainerProps } from '@/components/types/ContainerProps';
import { css } from '@/util/css';

export function Main({ className, ...rest }: ContainerProps) {
    return <main className={css('app', className)} {...rest}></main>;
}
