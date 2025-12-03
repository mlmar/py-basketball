import type { ContainerProps } from '@/components/types/ContainerProps';
import { css } from '@/util/css';

interface SectionProps extends ContainerProps {}

export function Section({ className = '', ...rest }: SectionProps) {
    return <section className={css('section', className)} {...rest}></section>;
}

interface SectionSubProps extends ContainerProps {}

Section.Sub = function ({ className, ...rest }: SectionSubProps) {
    return <p className={css('section-sub', className)} {...rest}></p>;
};
