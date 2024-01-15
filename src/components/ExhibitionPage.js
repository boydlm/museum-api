import React, { useState } from 'react';
import ExhibitionViewer from './ExhibitionViewer';
import MuseumSelect from './MusuemSelect';

export default function ExhibitionPage() {
    const [museum, setMuseum] = useState("")
    return (
        <div>
            <MuseumSelect onSelect={setMuseum} />
            <ExhibitionViewer museum={museum}
            />
        </div>

    );
}