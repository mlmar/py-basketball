import type { ContainerProps } from '@/components/types/ContainerProps';
import { css } from '@/util/css';

interface MainProps extends ContainerProps {}

export function Main({ className, ...rest }: MainProps) {
    return <main className={css('app', className)} {...rest}></main>;
}
