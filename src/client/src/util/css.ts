type CSSValue = null | undefined | string | string[] | {
    [key: string]: boolean
}

/**
 * Combines strings, array of strings and objects into a single class name string
 * @param {CSSValue[]} values 
 * @returns {string}
 */
export function css(...values: CSSValue[]): string {
    return values.reduce(cssReducer, '').trim();
}

/**
 * Parses incoming arguments and returns a className string
 * @param {string} result 
 * @param {CSSValue} value 
 * @returns {string}
 */
function cssReducer(result: string, value: CSSValue): string {
    if (!value) { // If no value is provided, return empty string
        return result;
    } else if (typeof value === 'string') { // If value is a string, concatenate the string
        return result + ' ' + value;
    } else if (Array.isArray(value)) { // If value is an array of string, then recurse on the array
        const arrayResult = css(value);
        if (arrayResult) {
            return result + ' ' + arrayResult;
        }
    } else if (typeof value === 'object') { // If value is an object, then recurse on the object pairs
        for (const key in value) {
            if (value[key]) { // If key value pair is true, then recurse on the key
                result = css(result, key);
            }
        }
    }
    return result
}